#include <stdio.h>
#include <string.h>

/*
 * Remove spaces from a string
 */
void removeSpace(char *str) {
    char *p1 = str, *p2 = str;
    /*
    int i, pos;
    char *p1 = str, *p2 = str;
    int space_count, pos = 0;
    for (i = 0; i < strlen(str); i++) {
        if (str[i] == ' ') {
            space_count++;
        }
    }
    printf("space count is: %i\n", space_count);
    int new_length = strlen(str) - space_count;
    printf("new length is: %i\n", new_length);
    char new_str[new_length-2];
    printf("new string is: %s\n", new_str);

    printf("print something\n");
    pos = 0;
    for (i = 0; i < strlen(p1) - 1; i++) {
        if (p1[i] != " ") {
            printf("print something\n");
            p2[pos] = p1[i];
            pos++;
        }
    }
    printf("%s", str);
    */
    do {
        while (*p2 == " ") {
            p2++;
        }
    } while (*p1++ = *p2++);
}

int main(int argc, char *argv[]) {
    printf("print something\n");
    char *str = "oh hi there";
    printf("string is: %s", str);
    removeSpace(str);
    printf("string is: %s", str);
    return 0;
}

