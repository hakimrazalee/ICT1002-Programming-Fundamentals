#include <stdio.h>
void exe_1();

int main() {
    exe_1();
}

void exe_1() {
    struct grade_node {
        char surname[20];
        double grade;
        struct grade_node *next;
    };
    typedef struct grade_node GRADE_NODE;
    typedef GRADE_NODE *GRADE_NODE_PTR;

    GRADE_NODE_PTR head = NULL; // initialise empty list
    GRADE_NODE node1 = {"Adams", 85.0, NULL};
    head = &node1;

    GRADE_NODE node2 = {"Pritchard", 66.5, NULL};
    GRADE_NODE node3 = {"Jones", 91.5, NULL};

    node1.next = &node3;
    node3.next = &node2;

    printf("The address of the first node in the list is: %p\n", head);

    while (head->next != NULL){
        printf("Name: %s, Grades: %0.1f\n", head->surname,head->grade);

        head = head->next;
    }
    printf("The last node is: \n");
    printf("Name: %s, Grades: %0.1f\n", head->surname, head->grade);

}

