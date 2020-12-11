#include <stdio.h>
#include <ctype.h>
#include <string.h>
#define MAXLETTERS 13 //Total number of letters allowed + 1 (buffer)
#define guessCount 7 //No of guesses allowed


int main() {
    int guessed = 0; //word guessed correctly flag
    int flag = 0; // word input correctly flag
    int count = guessCount; // Guess Counter
    char guess; // Player 2 input
    char userInput[MAXLETTERS]; // Player 1 input
    char wordProgress[MAXLETTERS]; // Guessing progress

    while (flag == 0){ // Checks if Player 1 has a valid input.
        printf("Player 1, enter a word of no more than %i letters:\n", MAXLETTERS - 1);
        fgets(userInput, MAXLETTERS, stdin);
        for (int i = 0; i<strlen(userInput)-1; i++){
            if (isalpha(userInput[i]) == 0){ // Checks if it is an English letter (a-z)
                flag = 0; // Sets flag to zero if it is not.
                printf("Sorry, the word must contain only English letters.\n");
                break; // breaks after finding one non-letter
            }
            else
            {
                flag = 1; // sets flag to 1 if all the letters have passed.
            }
            userInput[i] = tolower(userInput[i]);
        }
    }
    for (int j = 0; j < strlen(userInput) - 1; j++){
        strcpy(&wordProgress[j], "_"); //stores the _ value in an array.
    }
    for (int i = 0; i<count; i++){
        printf("Player 2 has so far guessed: ");
        for (int g = 0; g<strlen(wordProgress); g++){
            printf("%c ", wordProgress[g]); // prints out the progress in the specified format
        }
        printf("\nPlayer 2, you have %i guesses remaining. Enter your next guess:\n", count - i);
        scanf("%c%*c", &guess); //Removes the 'ENTER' new line from user input.
        int counted = 0; // Initialise counted flag
        for (int j = 0; j < strlen(userInput) - 1; j++){
            if (tolower(guess) == userInput[j]){
                wordProgress[j] = userInput[j];
                counted = 1; //If there is a match the flag will increase to prevent duplicate matches from affecting the guess count.
            }
        }
        if (counted == 1){ // Since a match was found, dont increment the guess count.
            count++;
        }
        for (int v = 0; v<strlen(userInput)-1; v++){
            if (wordProgress[v] == userInput[v]){ // Sets flag if all letters match the initial input by Player 1.
                guessed = 1;
            }
            else
            {
                guessed = 0;
                break;
            }
        }
        if (guessed == 1){ // If flag has been set, player 2 wins.
            printf("Player 2 has so far guessed: ");
            for (int g = 0; g<strlen(wordProgress); g++){
                printf("%c ", wordProgress[g]); // Output based on specified format.
            }
            printf("\nPlayer 2 wins.");
            break;
        }
    }
    if (guessed == 0 ){ // If guess flag has not been set after the number of guesses has ended, Player 1 wins.
        printf("Player 1 wins.");
    }
}
