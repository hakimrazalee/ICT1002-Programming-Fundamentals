#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX_LIMIT 255
int exe1();
int exe2();
int exe3();

int main(){
//    exe1();
//    exe2();
    exe3();
}

int exe3(){
    {// EXE_3: Character and Strings
        int x = 0,y = 0;
        char sentence[MAX_LIMIT];
        char wordFound[10][10]; //make new array for found words give some memory
        printf("Enter a sentence, up to 255 characters:\n");
        fgets(sentence, MAX_LIMIT, stdin); // take in all of it as one long string inclusive of whitespace

        for(int i = 0; i<strlen(sentence); i++) {
            if (sentence[i] == ' ' || sentence[i] == '\0'){
                wordFound[x][y] = '\0'; // end the word
                x++; // different row
                y=0; //reset indexy
            }
            else
            {
                if(isalnum(sentence[i])){
                    wordFound[x][y] = sentence[i]; //same row diff column
                    y++; // next column same word
                }


            }
        }
        int success = 0;
        for (int i = 0; i<=x; i++){
            printf("\n%s ", wordFound[i]);
            int length = strlen(wordFound[i]);
            printf("%i", length);

            if(strcmp(tolower(wordFound[i]), "the")==0){
                success = 1;
            };
        }
        if (success > 0){
            printf("\nYou said the magic word!");
            printf("\nThe magic word is 'The'");
        }
    }
}

int exe1(){ // EXE_1: Array Expressions
    int a[4] = { -1, 2, 10, 7 };
    int b[4];
    for (int i = 0; i < 4; i++)
        b[i] = a[3 - i];

    printf("%i\n",a[3]);
    printf("%i\n", b[3]);
    printf("%i\n", b[a[1]]);
}



int exe2(){// EXE_2: Character and String Expressions
    char *a = "abcdef";
    char b[7];
    strcpy(b, a); //Copy a into the array b
    for (int i = 0; i < 3; i++)
        b[i] = b[i] + 1;
    b[3] = '\0';

    printf("%c\n", a[0]);
//    printf("%i\n", a[0]); //ASCII VALUE
    printf("%c\n", b[0]);
//    printf("%i\n", b[0]); //ASCII VALUE
    printf("%c\n", b[4]);
//    printf("%i\n", b[4]); //ASCII VALUE
    printf("%i\n", strlen(a));
    printf("%i\n", strlen(b));
    printf("%i\n", strcmp(a, b));

}
