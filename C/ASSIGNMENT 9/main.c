#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX_LIMIT 255 //MAX CHARACTER LIMIT

void tinygrep(char textInput[MAX_LIMIT], char patternInput[MAX_LIMIT], const char caseSense[2]); //FUNCTION PROTOTYPE

int main() {
    char textInput[MAX_LIMIT];  //Initialise variables
    char patternInput[MAX_LIMIT];
    char caseSense[2];

    fgets(textInput, MAX_LIMIT, stdin); //gets user input including whitespaces
    scanf("%254s", patternInput); // gets user input
    scanf("%1s", caseSense); // gets user input
    tinygrep(textInput, patternInput, caseSense); // call function
}

void tinygrep(char textInput[MAX_LIMIT], char patternInput[MAX_LIMIT], const char caseSense[2]) { //Tinygrep function

    int i, j;
    int x = 0;
    int confirmedMatch = 0;
    int matchIndex;
    char foundWords[MAX_LIMIT];


    for (i = 0; i < strlen(textInput); i++) {
        if (caseSense[0] == 'N') { //If not case sensitive, make all of user-input words lowercase
            foundWords[x] = tolower(textInput[i]);
            x++; // next column same word
        } else if (caseSense[0] == 'Y') { // If case sensitive, leave it as it is
            foundWords[x] = textInput[i];
            x++; // next column same word
        }

    }
    for (i = 0; i < strlen(foundWords); i++) { //For every letter in the array/string
        if (textInput[i] == patternInput[0] || patternInput[0] == '.') { // If letter is a . or the same as the first letter of the pattern
            for (j = 0; j < strlen(patternInput); j++) { // For every letter in pattern

                if (patternInput[j] == '_') { //if the pattern is an _ make it a whitespace
                    patternInput[j] = ' ';
                }
                if (textInput[i + j] == patternInput[j] || patternInput[j] == '.') { //If pattern is equal to the current letter from user input we are checking
                    if (j == strlen(patternInput) - 1){ // of if pattern is a . // Check if the no of letters is the same as the no of letters in pattern (Excluding the null terminator)

                        matchIndex = i; //Assign the matched word index
                        confirmedMatch = 1; //set the flag to a found match
                        break; //break the loop
                    }
                }
            }
        }
        if (confirmedMatch == 1) { //If there is already a match dont have to check again.
            break;
        }
    }

    if (confirmedMatch == 1) { // If it is a confirmed match, print this else print no match.
        printf("Matches at position %i", matchIndex);
    } else{
        printf("No match.");
    }
}









