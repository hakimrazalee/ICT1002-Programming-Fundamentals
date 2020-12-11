#include <stdio.h>
#define LowestNum 1
#define HighestNum 1000
#define NoOfGuesses 10
#define LoopCounter 10 - 1 // 10 guesses so minus 1 to end after all 10 guesses are used up.
int main(){
    int number = 0; // Initialise the number that will be given by Player 1.

    printf("Player 1, enter a number between %i and %i:\n", LowestNum, HighestNum); // Uses the constant that is defined earlier.
    scanf("%i", &number); // Asks Player 1 for input.

    if (number >= LowestNum && number <= HighestNum ){ // Check if the number given by Player 1 is in range.
        int i; // Initialise for loop counter.
        int loopCounter = LoopCounter; // To check for invalid input
        int guess = 0; // Initialise the variable holding Player 2's guess.
        int guessCount = NoOfGuesses; // Initialise the guess counter.
        for (i = 0; i <= loopCounter; i++){ // Start the for loop.
            printf("Player 2, you have %i guesses remaining.\n", guessCount); // Displays the No of guesses Player 2 has.
            printf("Enter your guess:\n");
            scanf("%i", &guess);
            if (guess == number) { // Check if the guess is correct
                printf("Player 2 wins."); // If it is correct, loop ends.
                break;
            } else if (guess > HighestNum || guess < LowestNum){ //Check if guess is out of range.
                printf("That number is out of range.\n");
                guessCount = guessCount + 1; // Prevent guess count from incrementing.
                loopCounter = loopCounter + 1; // Ensures loop continues after invalid guess.
            } else if (guess < number){ // Check if guess is Too Low.
                printf("Too low.\n");
            } else if (guess > number){ // Check if guess is Too High.
                printf("Too high.\n");
            } else { // For any other input type.
                printf("That is not a valid input.\n");
            }
            guessCount = guessCount - 1; // No of Guesses decremented.
            if (guessCount == 0){ // If guess count reaches 0, player 2 loses.
                printf("Player 1 wins.");
            }
        }

    } else if (number < LowestNum || number > HighestNum){ // Check if number is out of range.
        printf("That number is out of range.\n");
        main(); // Restarts the program and prompts the user for a number again.
    }


//    return 0;
}