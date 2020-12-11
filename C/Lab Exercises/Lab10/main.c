#include <stdio.h>

void exe_1();
void exe_2();
void exe_3();

int main() {

//exe_1();
//exe_2();
exe_3();
}
void exe_3(){
    typedef struct {
        float value;
        char currency[3];

    } INTL_MONEY_VALUE;
/* initialise a variable of type student */
    INTL_MONEY_VALUE money1 = { 100.90, "SGD"};
    INTL_MONEY_VALUE money2 = { 128.23, "USD"};
    printf("%.2f %s\n", money1.value, money1.currency);
    printf("%.2f %s\n", money2.value, money2.currency);

    typedef INTL_MONEY_VALUE *INTL_MONEY_VALUE_PTR;
    INTL_MONEY_VALUE_PTR ptr1;
    ptr1 = &money1;
    printf("The pointed value (address) of ptr1 is : %p\n", ptr1);
    printf("The pointed value (address) of money1 is : %p\n", &money1);
}
void exe_1(){

    int *zPtr; /* zPtr will reference array z */
    int *aPtr = NULL;
    void *sPtr = NULL;
    int number, i;
    int z[ 5 ] = { 1, 2, 3, 4, 5 };
    zPtr = z;
    sPtr = z;


//    // Before Editing
//    /* use a pointer to get the first value of array */
//    number = zPtr;
//
//    /* assign array element 2 (the value 3) to number */
//    number = *zPtr[ 2 ];
//
//    /* print the entire array z */
//    for ( i = 0; i <= 5; i++ ) {
//        printf( "%d ", zPtr[ i ] );
//    }

    /* use a pointer to get the first value of array */
    number = *zPtr;
    printf("The first value of array z : %d\n", number);

    /* assign array element 2 (the value 3) to number */
    number = zPtr[ 2 ];
    printf("value of array element 2 is %d\n", number);

    /* print the entire array z */
    for ( i = 0; i < 5; i++ ) {
        printf( "%d ", zPtr[ i ] );
    }
}

void exe_2(){
    long value1 = 200000;
    long value2;
//    a) Define the variable lPtr to be a pointer to a variable of type long.
    long *lPtr;
//    b) Assign the address of variable value1 to pointer variable lPtr.
    lPtr = &value1;
//    c) Print the value of the variable pointed to by lPtr.
    printf("The value of the variable pointed to by lPtr is: %ld\n", *lPtr);
//    d) Assign the value of the variable pointed to by lPtr to variable value2.
    value2 = *lPtr;
//    e) Print the value of value2.
    printf("The value of value2 : %ld\n", value2);
//    f) Print the address of value1.
    printf("The address of the value1 is : %p\n", &value1);
//    g) Print the address stored in lPtr. Is the value printed the same as the address of value1?
    printf("The address stored in lPtr is : %p\n", lPtr);
}