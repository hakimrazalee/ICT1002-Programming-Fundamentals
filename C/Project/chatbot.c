/*
 * ICT1002 (C Language) Group Project.
 *
 * This file implements the behaviour of the chatbot. The main entry point to
 * this module is the chatbot_main() function, which identifies the intent
 * using the chatbot_is_*() functions then invokes the matching chatbot_do_*()
 * function to carry out the intent.
 *
 * chatbot_main() and chatbot_do_*() have the same method signature, which
 * works as described here.
 *
 * Input parameters:
 *   inc      - the number of words in the question
 *   inv      - an array of pointers to each word in the question
 *   response - a buffer to receive the response
 *   n        - the size of the response buffer
 *
 * The first word indicates the intent. If the intent is not recognised, the
 * chatbot should respond with "I do not understand [intent]." or similar, and
 * ignore the rest of the input.
 *
 * If the second word may be a part of speech that makes sense for the intent.
 *    - for WHAT, WHERE and WHO, it may be "is" or "are".
 *    - for SAVE, it may be "as" or "to".
 *    - for LOAD, it may be "from".
 * The word is otherwise ignored and may be omitted.
 *
 * The remainder of the input (including the second word, if it is not one of the
 * above) is the entity.
 *
 * The chatbot's answer should be stored in the output buffer, and be no longer
 * than n characters long (you can use snprintf() to do this). The contents of
 * this buffer will be printed by the main loop.
 *
 * The behaviour of the other functions is described individually in a comment
 * immediately before the function declaration.
 *
 * You can rename the chatbot and the user by changing chatbot_botname() and
 * chatbot_username(), respectively. The main loop will print the strings
 * returned by these functions at the start of each line.
 */

#include <stdio.h>
#include <string.h>
#include "chat1002.h"


/*
 * Get the name of the chatbot.
 *
 * Returns: the name of the chatbot as a null-terminated string
 */
const char *chatbot_botname() {

	return "Odin";

}


/*
 * Get the name of the user.
 *
 * Returns: the name of the user as a null-terminated string
 */
const char *chatbot_username() {

	return "Thor";

}


/*
 * Get a response to user input.
 *
 * See the comment at the top of the file for a description of how this
 * function is used.
 *
 * Returns:
 *   0, if the chatbot should continue chatting
 *   1, if the chatbot should stop (i.e. it detected the EXIT intent)
 */
int chatbot_main(int inc, char *inv[], char *response, int n) {

	/* check for empty input */
	if (inc < 1) {
		snprintf(response, n, "");
		return 0;
	}

	/* look for an intent and invoke the corresponding do_* function */
	if (chatbot_is_exit(inv[0]))
		return chatbot_do_exit(inc, inv, response, n);
	else if (chatbot_is_smalltalk(inv[0]))
		return chatbot_do_smalltalk(inc, inv, response, n);
	else if (chatbot_is_load(inv[0]))
		return chatbot_do_load(inc, inv, response, n);
	else if (chatbot_is_question(inv[0]))
		return chatbot_do_question(inc, inv, response, n);
	else if (chatbot_is_reset(inv[0]))
		return chatbot_do_reset(inc, inv, response, n);
	else if (chatbot_is_save(inv[0]))
		return chatbot_do_save(inc, inv, response, n);
	else {
		snprintf(response, n, "I don't understand \"%s\".", inv[0]);
		return 0;
	}

}


/*
 * Determine whether an intent is EXIT.
 *
 * Input:
 *  intent - the intent
 *
 * Returns:
 *  1, if the intent is "exit" or "quit"
 *  0, otherwise
 */
int chatbot_is_exit(const char *intent) {

	return compare_token(intent, "exit") == 0 || compare_token(intent, "quit") == 0;

}


/*
 * Perform the EXIT intent.
 *
 * See the comment at the top of the file for a description of how this
 * function is used.
 *
 * Returns:
 *   0 (the chatbot always continues chatting after a question)
 */
int chatbot_do_exit(int inc, char *inv[], char *response, int n) {
	knowledge_reset();
	snprintf(response, n, "Goodbye!");

	return 1;

}


/*
 * Determine whether an intent is LOAD.
 *
 * Input:
 *  intent - the intent
 *
 * Returns:
 *  1, if the intent is "load"
 *  0, otherwise
 */
int chatbot_is_load(const char* intent) {

	/* to be implemented */

	if (compare_token(intent, "load")) {		// Checks if the intent given is "LOAD". It will return 1 if intent is "LOAD" and 0 if it is not

		return 0;
	}
	else {

		return 1;
	}
}


/*
 * Load a chatbot's knowledge base from a file.
 *
 * See the comment at the top of the file for a description of how this
 * function is used.
 *
 * Returns:
 *   0 (the chatbot always continues chatting after loading knowledge)
 */
int chatbot_do_load(int inc, char* inv[], char* response, int n) {

	/* to be implemented */

	int num = 0;

	if (inv[1] == NULL) {

		strcpy(response, "No file found!");												// If inv[1] is NULL, it will return the error message into the response
	}
	else {
		FILE* file;																		// Declare a pointer to a FILE structure
		if (file = fopen(inv[1], "r")) {												// Open the file to read using fopen()
			num = knowledge_read(file);													// Read the number of lines in the file
			fclose(file);																// Close the file using fclose()
			snprintf(response, n, "Read %d responses from %s", num, inv[1]);
		}
		else {
			strcpy(response, "No such file!");											// If no such file is found, it will return the error message into the response
		}
	}

	return 0;

}


/*
 * Determine whether an intent is a question.
 *
 * Input:
 *  intent - the intent
 *
 * Returns:
 *  1, if the intent is "what", "where", or "who"
 *  0, otherwise
 */
int chatbot_is_question(const char* intent) {

	/* to be implemented */

	if (compare_token(intent, "what") == 0 || compare_token(intent, "where") == 0 || compare_token(intent, "who") == 0) {
		return 1;																		// Checks if the intent given is a "WHAT" or "WHERE" or "WHO" question. Returns 1 if it is a
	}																					// "WHAT" or "WHERE" or "WHO" question and returns 0 if it is not.
	return 0;

}


/*
 * Answer a question.
 *
 * inv[0] contains the the question word.
 * inv[1] may contain "is" or "are"; if so, it is skipped.
 * The remainder of the words form the entity.
 *
 * See the comment at the top of the file for a description of how this
 * function is used.
 *
 * Returns:
 *   0 (the chatbot always continues chatting after a question)
 */
int chatbot_do_question(int inc, char* inv[], char* response, int n) {

	/* to be implemented */

	char userInputIntent[MAX_INTENT];															// Creates an array "userInputIntent" with size of maximum intent length
	strncpy(userInputIntent, inv[0], sizeof(userInputIntent) / sizeof(userInputIntent[0]));		// Copy inv[0] into userInputIntent, with number of characters copied = sizeof(userInputIntent) / sizeof(userInputIntent[0])
	char userInputNoun[MAX_INPUT];																// Creates an array "userInputNoun" with size of maximum input of noun length
	strcpy(userInputNoun, "\0");																// Copy NULL value into userInputNoun

	char userInputEntity[MAX_ENTITY];															// Creates an array "userInputEntity" with size of maximum entity
	snprintf(userInputEntity, n, "");															// Change the entity

	int knowledgeGetFlag;																		// Create an integer to store return value from function knowledge_get
	char entityFromChatBot[MAX_RESPONSE];														// Creates an array with size of maximum response length to store response
	char noResponse[MAX_RESPONSE];																// Creates an array with size of maximum response length to store user input

	int knowledgePutFlag;																		// Creates an integer to store return value from function knowledge_put


	if (inc == 1) {
		if (compare_token(userInputIntent, "what") == 0) {																							// Checks if intent is "what" or not
			snprintf(response, n, "Sorry, I did not understand the phrase. Did you mean something like, \"What is ICT?\"");							// Print error msg
		}
		else if (compare_token(userInputIntent, "who") == 0) {																						// Checks if intent is "who" or not
			snprintf(response, n, "Sorry, I did not understand the phrase. Did you mean something like, \"Who is the cluster director of ICT?\"");	// Print error msg
		}
		else if (compare_token(userInputIntent, "where") == 0) {																					// Checks if intent is "where" or not
			snprintf(response, n, "Sorry, I did not understand the phrase. Did you mean something like, \"Where is SIT?\"");						// Print error msg
		}
		return 0;
	}
	else if ((inc == 2 && compare_token(inv[1], "is") == 0) || (inc == 2 && compare_token(inv[1], "are") == 0)) {									// Checks for "is" or "are"
		snprintf(response, n, "Sorry, I did not understand the phrase. Please describe your noun.");												// Print error msg
		return 0;
	}


	for (int i = 1; i < inc; i++) {
		if ((i == 1 && compare_token(inv[i], "is") == 0) || (i == 1 && compare_token(inv[i], "are") == 0)) {		// Check for "is" or "are"
			strncpy(userInputNoun, inv[i], sizeof(inv[i]) / sizeof(inv[i][0]));										// Copy string to userInputNoun
			continue;
		}
		strcat(strcat(userInputEntity, " "), inv[i]);																// Add space and inv[i] to userInputEntity
	}
	memmove(userInputEntity, userInputEntity + 1, strlen(userInputEntity));											// Move userInputEntity + 1 into userInputEntity with size of userInputEntity length


	knowledgeGetFlag = knowledge_get(userInputIntent, userInputEntity, entityFromChatBot, n);						// Store flag into knowledge_get return result
	if (knowledgeGetFlag == KB_OK) {																				// Check if KB_OK
		snprintf(response, n, "%s", entityFromChatBot);																// Copy response

	}
	else if (knowledgeGetFlag == KB_NOTFOUND) {																		// Check if KB_NOTFOUND
		if (compare_token(userInputNoun, "\0") == 0) {																// Check if userInputNoun is NULL
			prompt_user(noResponse, MAX_INPUT, "I don't know. %s %s?", userInputIntent, userInputEntity);			// Ask for user input
		}
		else {
			prompt_user(noResponse, MAX_INPUT, "I don't know. %s %s %s?", userInputIntent, userInputNoun, userInputEntity);	// Ask for user input
		}

		if (strcmp(noResponse, "") == 0) {
			strcpy(response, "-(");
		}
		else {

			knowledgePutFlag = knowledge_put(userInputIntent, userInputEntity, noResponse);		// Store flag from knowledge_put return result

			if (knowledgePutFlag == KB_OK) {													// Check if KB_OK
				snprintf(response, n, "Thank you.");											// Add msg to response
			}
			else if (knowledgePutFlag == KB_NOMEM) {											// Check if KB_NOMEM
				snprintf(response, n, "Memory allocation failure! Failed to create note for:\nIntent '%s'\nEntity '%s'\nResponse '%s'\n", userInputIntent, userInputEntity, noResponse); // Add msg to response
				exit(1);
			}
			else if (knowledgePutFlag == KB_INVALID) {											// Check if KB_INVALID
				snprintf(response, n, "Sorry, I didn't get '%s'.", userInputIntent);			// Add msg to response
			}
		}

	}
	else if (knowledgeGetFlag == KB_INVALID) {													// Check if KB_INVALID
		snprintf(response, n, "Sorry, I didn't get '%s'.", userInputIntent);					// Add msg to response
	}


	return 0;

}


/*
 * Determine whether an intent is RESET.
 *
 * Input:
 *  intent - the intent
 *
 * Returns:
 *  1, if the intent is "reset"
 *  0, otherwise
 */
int chatbot_is_reset(const char* intent) {

	/* to be implemented */
	if (compare_token(intent, "reset") == 0) {
		return 1;
	}

	return 0;


}


/*
 * Reset the chatbot.
 *
 * See the comment at the top of the file for a description of how this
 * function is used.
 *
 * Returns:
 *   0 (the chatbot always continues chatting after beign reset)
 */
int chatbot_do_reset(int inc, char* inv[], char* response, int n) {
	knowledge_reset();
	snprintf(response, n, "Chatbot reset.");
	return 0;
	int numReset = 0;

	if (headWho != NULL) {								// If linked list WHO is not empty
		baseNode* temp = headWho;					// Create pointer pointing to head of linked list WHO
		while (temp != NULL) {								// While temp is not NULL
			printf("\nRemoving Node '%s' '%s\n'", temp->intent, temp->entity);
			temp = temp->next;								// Go to next node
			free(headWho);								// Free head of linked list WHO
			headWho = temp;								// Change head of linked list WHO to the next node
		};
		numReset++;
	}

	if (headWhat != NULL) {								// If linked list WHAT is not empty
		baseNode* temp = headWhat;					// Create pointer pointing to head of linked list WHAT
		while (temp != NULL) {								// While temp is not NULL
			printf("\nRemoving Node '%s' '%s\n'", temp->intent, temp->entity);
			temp = temp->next;								// Go to next node
			free(headWhat);								// Free head of linked list WHAT
			headWhat = temp;								// Change head of linked list WHAT to the next node
		};
		numReset++;
	}

	if (headWhere != NULL) {								// If linked list WHERE is not empty
		baseNode* temp = headWhere;					// Create pointer pointing to head of linked list WHERE
		while (temp != NULL) {												// While temp is not NULL
			printf("\nRemoving Node '%s' '%s\n'", temp->intent, temp->entity);
			temp = temp->next;								// Go to next node
			free(headWhere);								// Free head of linked list WHERE
			headWhere = temp;								// Change head of linked list WHERE to the next node
		};
		numReset++;
	}

	if (numReset == 0) {									// Checks if there is resets or not
		snprintf(response, n, "There is nothing to reset.");
	}
	else {
		snprintf(response, n, "Chatbot reset.");
	}

	return 0;

}


/*
 * Determine whether an intent is SAVE.
 *
 * Input:
 *  intent - the intent
 *
 * Returns:
 *  1, if the intent is "what", "where", or "who"
 *  0, otherwise
 */
int chatbot_is_save(const char *intent) {

	/* to be implemented */
	if (compare_token(intent,"save")){       // Intent = SAVE
        return 0;                           // Return 0 if Intent is to SAVE
    }
    else {
        return 1;                      // Return 1 if intent not to SAVE
    }

	return 0;

}


/*
 * Save the chatbot's knowledge to a file.
 *
 * See the comment at the top of the file for a description of how this
 * function is used.
 *
 * Returns:
 *   0 (the chatbot always continues chatting after saving knowledge)
 */
int chatbot_do_save(int inc, char *inv[], char *response, int n) {

	/* to be implemented */
	char fileName[64];

    if (inv[1] == NULL){
        strcpy(response,"No file specified!");                   // Response if no file name specified
    }
    else if (headWhere == NULL && headWhat == NULL && headWho == NULL) {
    	strcpy(response, "No data to be saved!");                 // Response if no content/data to save
    }
    else{

    	strcpy(fileName, inv[1]);

    	int num;
   		FILE *fptr;
   		fptr = fopen(fileName, "w");
    	if(fptr == NULL){
			strcpy(response,"Error creating file");
		}
		else {
			knowledge_write(fptr);
    		snprintf(response, n, "My knowledge has been saved to %s.", fileName);
		}

		fclose(fptr);



    }

	return 0;

}


/*
 * Determine which an intent is smalltalk.
 *
 *
 * Input:
 *  intent - the intent
 *
 * Returns:
 *  1, if the intent is the first word of one of the smalltalk phrases
 *  0, otherwise
 */
int chatbot_is_smalltalk(const char* intent) {

	/* to be implemented */
	return

		compare_token(intent, "Hello") == 0 ||
		compare_token(intent, "Greetings") == 0 ||
		compare_token(intent, "Hi") == 0 ||
		compare_token(intent, "Yo") == 0 ||
		compare_token(intent, "Help") == 0 ||

		// Informal Small Talk
		compare_token(intent, "Father") == 0 ||
		compare_token(intent, "Odin") == 0 ||
		compare_token(intent, "Mjolnir") == 0 ||
		compare_token(intent, "Hela") == 0


		;

}


/*
 * Respond to smalltalk.
 *
 * See the comment at the top of the file for a description of how this
 * function is used.
 *
 * Returns:
 *   0, if the chatbot should continue chatting
 *   1, if the chatbot should stop chatting (e.g. the smalltalk was "goodbye" etc.)
 */
int chatbot_do_smalltalk(int inc, char* inv[], char* response, int n) {


	if (compare_token("Help", inv[0]) == 0) {
		snprintf(response, n, "Try asking me some questions or engage in small talk!", chatbot_username());

	}
	else if (compare_token("Greetings", inv[0]) == 0) {
		snprintf(response, n, "Greetings, %s!", chatbot_username());

	}
	else if (compare_token("Hi", inv[0]) == 0) {
		snprintf(response, n, "Hi, %s!", chatbot_username());

	}
	else if (compare_token("Yo", inv[0]) == 0) {
		snprintf(response, n, "Have some manners! Give proper salutations, %s!", chatbot_username());

	}
	else if (compare_token("Hello", inv[0]) == 0) {
		snprintf(response, n, "Salutations, %s.", chatbot_username());


		// Informal Small Talk
	}
	else if (compare_token("Hela", inv[0]) == 0) {
		snprintf(response, n, "Do not speak of your sister's name, %s!", chatbot_username());

	}
	else if (compare_token("Father", inv[0]) == 0) {
		snprintf(response, n, "What is it, %s?", chatbot_username());

	}
	else if (compare_token("Odin", inv[0]) == 0) {
		snprintf(response, n, "You dare call me by my name!?");

	}
	else {
		snprintf(response, n, "Whosoever holds this hammer, if he be worthy, shall possess the power of Thor.", chatbot_username());
	}

	return 0;

}
