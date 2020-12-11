#include <stdio.h>
#include <string.h>



//int main() {
//    int a = -1, b = 2;
//    float x = 0.1;
//    float y = 1.5;
//    char c = 'p';
////exe 2A
//    printf("%d\n",a/b);
//    printf("%d\n", a*b);
//    printf("%d\n", (b*3)%4);
//    printf("%.1f\n", x*a);
//    printf("%f\n", x*y);
//    printf("%f\n", y/x);
//    printf("%d\n",c-3);
//
//////Exe2 b)
////printf("%4d\n", a);
////printf("%04d\n", b);
////printf("a/b = %d\n", a/b);
////printf("%x\n", b);
////printf("%.2f\n", y);
////printf("%10.1f\n", x);
////printf("c=\t%c\n", c);
////
////
//}

//exe 3
int main(){
    float w = 0;
    float h = 0;

    printf("Enter your Weight (in kilograms):\n");
    scanf("%f", &w);

    printf("Enter your Height (in metres):\n");
    scanf("%f", &h);

    float x = w/(h*h);

    if(x < 18.5){
        printf("Your BMI is %.1f That is within the underweight range.", x);
    } else if (x > 18.5 & x < 24.9){
        printf("Your BMI is %.1f. That is within the Normal range.", x);
    } else if (x > 25.0 & x <29.9){
        printf("Your BMI is %.1f That is within the Overweight range.", x);
    } else {
        printf("Your BMI is %.1f That is within the Obese range.", x);
    }
    return 0;
}


