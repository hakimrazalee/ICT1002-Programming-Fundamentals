#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NAMSIZ 100

struct header {
    char name[NAMSIZ];
    char size[12];
};

typedef struct header HEADER;
typedef HEADER * HEADER_PTR;

int main(int argc, char ** argv) {

    int s_header = sizeof(HEADER);
    char buffer[100];
    FILE * archive;
    long lSize;
    archive = fopen("result.tar", "w");
    for (int i = 1; i < argc; i++) {
        char * filename = argv[i];
        FILE * fp;
        fp = fopen(filename, "r");
        if (fp == NULL) {
            printf("Error opening file\n");
        }
        HEADER_PTR FILE_HEAD = malloc(s_header);
        // obtain file size:
        fseek (fp , 0 , SEEK_END);
        lSize = ftell (fp);
        rewind (fp);
        itoa(lSize, buffer, 10);
        printf("%s",buffer);
        strcpy(FILE_HEAD->name,filename);
        strcpy(FILE_HEAD->size,buffer);
        fseek(fp, 0, SEEK_END);
        fwrite(FILE_HEAD, s_header, 1, archive);
        // END OF FILE HEADER

        // COPYING OF FILE CONTENTS
        fseek(fp, 0, SEEK_SET);
        while (!feof(fp)) {
            fputc(fgetc(fp), archive);
        }
        free(FILE_HEAD);
        fclose(fp);
    }
    fclose(archive);
    return 0;
}