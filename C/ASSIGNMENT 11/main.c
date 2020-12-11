#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define characterLimit 32

struct node { //create the node struct
    char *data;
    struct node *next;
};

typedef struct node NODE;
typedef NODE * NODE_PTR;


int main(){

    NODE_PTR head = NULL; //make an empty list
    int flag = 0;

    do {
        char *input = (char *) malloc(characterLimit* sizeof(char)); //dynamic allocation of memory
        if (input == NULL) { //memory handling
            printf("Out of memory.");
            return 1;
        }
//        printf("Please enter a word: ");
        fgets(input, characterLimit, stdin);
        input = strtok(input, "\n"); //removes the new line taken by fgets

        if (strcmp(input, "***") == 0) {
            printf("All the entered words in order:");

            while (head != NULL) {
                printf("%s\n", head->data);
                head = head->next;
            }
            free(input);

            break;
        }

        for (int i = 0; (i < strlen(input)); i++){
            if (isalpha(input[i]) != 0 || input[i] == '-' || input[i] == '\'') {
                input[i] = tolower(input[i]);
                flag = 1;
            }
            else
            {
                flag = 0;
                printf("Invalid Input\n");
                break;
            }
        }

        if (flag == 1) {

            NODE_PTR current = (NODE_PTR) malloc(2* sizeof(NODE));
            if (current == NULL) {
                printf("Out of memory.");
                return 1;
            }
            current->data = input;
            current->next = NULL;

            if (head == NULL) {
                head = current;
                continue;
            }
            NODE_PTR temp = head;
            NODE_PTR prev = NULL;
            int found = 0;
            while (temp != NULL) {
                if (strcmp(input, temp->data) < 0) {
                    found = 1;
                    if (prev == NULL) {
                        current->next = head;
                        head = current;
                    } else {
                        current->next = temp;
                        prev->next = current;
                    }
                    break;
                }
                prev = temp;
                temp = temp->next;
            }

            if (!found) {
                prev->next = current;

            }

        }


    } while (1);
    return 0;
}