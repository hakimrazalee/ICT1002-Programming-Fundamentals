/*
 * ICT1002 (C Language) Group Project.
 *
 * This file implements the chatbot's knowledge base.
 *
 * knowledge_get() retrieves the response to a question.
 * knowledge_put() inserts a new response to a question.
 * knowledge_read() reads the knowledge base from a file.
 * knowledge_reset() erases all of the knowledge.
 * knowledge_write() saves the knowledge base in a file.
 *
 * You may add helper functions as necessary.
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "chat1002.h"

 /*
  * Get the response to a question.
  *
  * Input:
  *   intent   - Who, what or where
  *   entity   - the entity
  *   response - a buffer to receive the response
  *   n        - the maximum number of characters to write to the response buffer
  *
  * Returns:
  *   KB_OK, if a response was found for the intent and entity (the response is copied to the response buffer)
  *   KB_NOTFOUND, if no response could be found
  *   KB_INVALID, if 'intent' is not a recognised question word
  */
int knowledge_get(const char* intent, const char* entity, char* response, int n) {

    if (compare_token(intent, "who") == 0) {                                        // This line is to check whether the intent is a "who" question or not
        if (headWho != NULL) {                                                    // This line checks if there is a linked list for "who"
            iterateWho = headWho;                                                // This line will put the iterateWho as the head to the linked list
            while (iterateWho) {
                if (compare_token(iterateWho->entity, entity) == 0) {              // This line will check whether the entity is equal
                    strncpy(response, iterateWho->response, n);                    // This line will copy the response if the entity is equal (Basically getting the answer to the question)
                    return KB_OK;                                                   // This line will return the response found
                }
                iterateWho = iterateWho->next;                                    // This line will move the iterateWho to the next node if entity is different
            };
            return KB_NOTFOUND;                                                     // This line will activate if no response could be found
        }
        else if (headWho == NULL) {
            return KB_NOTFOUND;                                                     // This line will activate if no response could be found
        }
    }

    else if (compare_token(intent, "what") == 0) {                                  // This line is to check whether the intent is a "what" question or not
        if (headWhat != NULL) {                                                   // This line checks if there is a linked list for "what"
            iterateWhat = headWhat;                                              // This line will put the iterateWhat as the head to the linked list
            while (iterateWhat) {
                if (compare_token(iterateWhat->entity, entity) == 0) {             // This line will check whether the entity is equal
                    strncpy(response, iterateWhat->response, n);                   // This line will copy the response if the entity is equal (Basically getting the answer to the question)
                    return KB_OK;                                                   // This line will return the response found
                }
                iterateWhat = iterateWhat->next;                                  // This line will move the iterateWho to the next node if entity is different
            };
            return KB_NOTFOUND;                                                     // This line will activate if no response could be found
        }
        else if (headWhat == NULL) {
            return KB_NOTFOUND;                                                     // This line will activate if no response could be found
        }
    }

    else if (compare_token(intent, "where") == 0) {                                 // This line is to check whether the intent is a "where" question or not
        if (headWhere != NULL) {                                                  // This line checks if there is a linked list for "where"
            iterateWhere = headWhere;                                            // This line will put the iterateWho as the head to the linked list
            while (iterateWhere) {
                if (compare_token(iterateWhere->entity, entity) == 0) {            // This line will check whether the entity is equal
                    strncpy(response, iterateWhere->response, n);                  // This line will copy the response if the entity is equal (Basically getting the answer to the question)
                    return KB_OK;                                                   // This line will return the response found
                }
                iterateWhere = iterateWhere->next;                                // This line will move the iterateWhere to the next node if entity is different
            };
            return KB_NOTFOUND;                                                     // This line will activate if no response could be found
        }
        else if (headWhere == NULL) {
            return KB_NOTFOUND;                                                     // This line will activate if no response could be found
        }
    }
    else {
        return KB_INVALID;                                                          // This line will activate if 'intent' is not a recognised question word
    }
}


/*
 * Insert a new response to a question. If a response already exists for the
 * given intent and entity, it will be overwritten. Otherwise, it will be added
 * to the knowledge base.
 *
 * Input:
 *   intent    - the question word
 *   entity    - the entity
 *   response  - the response for this question and entity
 *
 * Returns:
 *   KB_FOUND, if successful
 *   KB_NOMEM, if there was a memory allocation failure
 *   KB_INVALID, if the intent is not a valid question word
 */
int knowledge_put(const char *intent, const char *entity, const char *response) {

                                                                                //creating buffer
    char response_temp[MAX_RESPONSE];
                                                                                //store result of knowledge_get()
    int get_output = knowledge_get(intent,entity,response_temp, MAX_RESPONSE);
                                                                                //clear the buffer
    memset(response_temp,'\0',MAX_RESPONSE);

                                                                                /* Return KB_INVALID if intent is invalid */
    if (get_output == -2){
        return KB_INVALID;
    }

                                                                                /* Else, either overwrite or insert the node depending on the return code, and the Intent */
    else{
                                                                                //check if the intent is WHAT
        if (compare_token(intent, "what") == 0) {
                                                                                //  If the intent has the entity
            switch(get_output) {
            case 0:
                iterateWhat = headWhat;
                do {
                                                                                //if the response for the question exist
                    if (compare_token(iterateWhat->entity, entity) == 0) {
                                                                                //replace the old response with entered response
                        strncpy(iterateWhat->response, response, MAX_RESPONSE);
                                                                                // returns the flag KB_OK, value 0, meaning end of function
                        return KB_OK;
                    }

                    iterateWhat = iterateWhat->next;
                } while (iterateWhat);
                break;

                                                                                //  If the intent does NOT have the entity
            case -1:
                {
                                                                                //create node
                baseNode *temp = (baseNode *)malloc(sizeof(baseNode));
                                                                                // If not enough memory (memory failure)
                if (temp == NULL) {
                                                                                // Return flag KB_NOMEM, value -4
                    return KB_NOMEM;
                }
                                                                                //copying the intent to the node's intent
                strcpy(temp->intent, intent);
                                                                                //copying the entity to the node's entity
                strcpy(temp->entity, entity);
                                                                                //copying the response to the node's response
                strcpy(temp->response, response);
                                                                                //set the next pointer of the node to the existing head
                temp->next = headWhat;
                                                                                //set the node as the new head
                headWhat = temp;

                                                                                //set flag to KB_OK, value 0
                return KB_OK;
                }


            }



        }
                                                                                //check if the intent is WHERE
        else if (compare_token(intent, "where") == 0) {
                                                                                //  If the intent has the entity
            switch(get_output) {
            case 0:
                iterateWhere = headWhere;
                do {
                                                                                //if the response for the question exist
                    if (compare_token(iterateWhere->entity, entity) == 0) {
                                                                                //replace the old response with entered response
                        strncpy(iterateWhere->response, response, MAX_RESPONSE);
                                                                                // returns the flag KB_OK, value 0, meaning end of function
                        return KB_OK;
                    }

                    iterateWhere = iterateWhere->next;
                } while (iterateWhere);
                break;

                                                                                //  If the intent does NOT have the entity
            case -1:
                {
                                                                                //create node
                    baseNode *temp = (baseNode *)malloc(sizeof(baseNode));
                                                                                // If not enough memory (memory failure)
                    if (temp == NULL) {
                                                                                // Return flag KB_NOMEM, value -4
                        return KB_NOMEM;
                    }
                                                                                //copying the intent to the node's intent
                    strcpy(temp->intent, intent);
                                                                                //copying the entity to the node's entity
                    strcpy(temp->entity, entity);
                                                                                //copying the response to the node's response
                    strcpy(temp->response, response);
                                                                                //set the next pointer of the node to the existing head
                    temp->next = headWhere;
                                                                                //set the node as the new head
                    headWhere = temp;

                                                                                //set flag to KB_OK, value 0
                    return KB_OK;

                }

            }

        }
                                                                                //check if the intent is WHO
        else if (compare_token(intent, "who") == 0){
                                                                                //  If the intent has the entity
            switch(get_output) {
            case 0:
                iterateWho = headWho;
                do {
                                                                                //if the response for the question exist
                    if (compare_token(iterateWho->entity, entity) == 0) {
                                                                                //replace the old response with entered response
                        strncpy(iterateWho->response, response, MAX_RESPONSE);
                                                                                // returns the flag KB_OK, value 0, meaning end of function
                        return KB_OK;
                    }

                    iterateWho = iterateWho->next;
                } while (iterateWho);
                break;

                                                                                //  If the intent does NOT have the entity
            case -1:
                {
                                                                                //create node
                    baseNode *temp = (baseNode *)malloc(sizeof(baseNode));
                                                                                // If not enough memory (memory failure)
                    if (temp == NULL) {
                                                                                // Return flag KB_NOMEM, value -4
                        return KB_NOMEM;
                    }
                                                                                //copying the intent to the node's intent
                    strcpy(temp->intent, intent);
                                                                                //copying the entity to the node's entity
                    strcpy(temp->entity, entity);
                                                                                //copying the response to the node's response
                    strcpy(temp->response, response);
                                                                                //set the next pointer of the node to the existing head
                    temp->next = headWho;
                                                                                //set the node as the new head
                    headWho = temp;

                                                                                //set flag to KB_OK, value 0
                    return KB_OK;
                }



            }
        }


    }

}



/*
 * Read a knowledge base from a file.
 *
 * Input:
 *   f - the file
 *
 * Returns: the number of entity/response pairs successful read from the file
 */
int knowledge_read(FILE *f) {
    int numOfLines = 0;
    char intent[MAX_INPUT], entity[MAX_ENTITY];
//    f = fopen(f, "r"); //opens the file
    if(f == NULL){ //check if there is such a file
        perror("Unable to open file!");
        exit(1);
    }
    char buf[MAX_ENTITY + MAX_RESPONSE]; //size of array to store the line

    //store chunks of text into a line buffer just in case the length of the line is longer than buf array
    size_t len = sizeof(buf);
    char *line = malloc(len);
    if(line == NULL){
        perror("Unable to allocate mem for the line buffer.");
        exit(1);
    }

    line[0] = '\0'; //empty line. \0 delimiter clears the rest of the array
    while(fgets(buf, sizeof(buf), f) != NULL){ // as long as there is something to output
        //Resize line buffer if necessary
        size_t len_used = strlen(line);
        size_t buf_used = strlen(buf);

        if(len - len_used < buf_used){ //check if the line in the file is longer than the size of array to store the line
            len *=2; //if yes multiply the size to 2
            if((line = realloc(line, len)) == NULL) { //reallocate new memory size
                perror("Unable to reallocate memory for the line buffer.");
                free(line);
                exit(1);
            }

        }

        strncpy(line + len_used, buf, len - len_used);
        len_used += buf_used;

        if(compare_token(line,"[what]\n") == 0){
            strcpy(intent, "WHAT");    // Copies the string pointed to from src to dest in this case dest is intent
        }
        else if(compare_token(line,"[where]\n") == 0){
            strcpy(intent, "WHERE");
        }
        else if(compare_token(line,"[who]\n") == 0){
            strcpy(intent, "WHO");
        }

        // To remove the entities from the line and store it by copying it to entity;
        strcpy(entity, strtok(line, "="));
        // To remove the response | str token allocates mem for us
        char *response = strtok(NULL, "");

        //check if line contains '\n', if yes process the line of text
        if(line[len_used - 1] == '\n' ){
            if(compare_token(intent,"\0") != 0 && compare_token(entity,"\0") != 0 && response != NULL){

                numOfLines++;
 //               printf("%s is %s? %s",intent,entity,response);
                knowledge_put(intent,entity,response);
            }


            line[0] = '\0';
        }

    }
    free(line);

    return numOfLines;
}



/*
 * Reset the knowledge base, removing all know entitities from all intents.
 */
void knowledge_reset() {

    /* to be implemented */
     if (headWho!=NULL){                         //check if headWho not null
         iterateWho = headWho;                   //point iterateWho to headWho location

	    while (headWho!=NULL){                     //While headOfWho not empty
            headWho= headWho->next;                      // Point headOfWHO to the next node
	        free(iterateWho);                              // Free the current node pointed
            iterateWho = headWho;                          //iterateWho now points to next node
	    }
	}
	if (headWhat !=NULL){                                  //check if headWhat not null
        iterateWhat = headWhat;                          //point iterateWhat to headWhat location

        while (headWhat !=NULL){                           //While headWhat not empty
            headWhat = headWhat->next;                    // Point headWhat to the next node
            free(iterateWhat);                             // Free the current node pointed
            iterateWhat = headWhat;                        //iterateWhat now points to next node
        }
    }

    if (headWhere !=NULL){                                 //check if headWhere not null
        iterateWhere = headWhere;                        //point iterateWhere to headWhere location

        while (headWhere !=NULL){                           //While headWhere not empty
            headWhere = headWhere->next;                  // Point headWhere to the next node
            free(iterateWhere);                            // Free the current node pointed
            iterateWhere = headWhere;                      //iterateWhere now points to next node
        }
    }

}


/*
 * Write the knowledge base to a file.
 *
 * Input:
 *   f - the file
 */
void knowledge_write(FILE *f) {

    /* to be implemented */
    if (headWho != NULL) {                                    //Determine whether there was responses to questions
        baseNode* temp = headWho;
        fprintf(f, "[%s]\n", "who");
        while (temp != NULL) {
            fprintf(f, "%s=", temp->entity);                    //Prints the values in the format Entity=Response
            fprintf(f, "%s\n", temp->response);
            temp = temp->next;
        }
        if (temp == NULL) {
            fprintf(f, "END.\n");                               //End of 1 piece of information, prints a new line for easy reading
        }
    }

    if (headWhat != NULL) {
        baseNode* temp = headWhat;
        fprintf(f, "[%s]\n", "what");
        while (temp != NULL) {
            fprintf(f, "%s=", temp->entity);
            fprintf(f, "%s\n", temp->response);
            temp = temp->next;
        }
        if (temp == NULL) {
            fprintf(f, "END.\n");
        }
    }

    if (headWhere != NULL) {
        baseNode* temp = headWhere;
        fprintf(f, "[%s]\n", "where");
        while (temp != NULL) {
            fprintf(f, "%s=", temp->entity);
            fprintf(f, "%s\n", temp->response);
            temp = temp->next;
        }
        if (temp == NULL) {
            fprintf(f, "END.\n");
        }
    }






}
