#include <stdio.h>
#include <ctype.h>

#define SPECIAL_CHAR(c) case c: printf(#c); break;

#define LINE_LENGTH 80

int print_char(char c) {
    switch(c) {
    SPECIAL_CHAR('\a')
    SPECIAL_CHAR('\b')
    SPECIAL_CHAR('\t')
    SPECIAL_CHAR('\v')
    SPECIAL_CHAR('\f')
    SPECIAL_CHAR('\r')
    SPECIAL_CHAR('\0')
    SPECIAL_CHAR('\\')
    default:
        if (isprint(c) || c == '\n') {
            putchar(c);
            return 1;
        }
        else return printf("\\%02x", c);
    }
    return 4;
}

int main() {
    int c;
    int l = 0;
    while ((c = getchar()) != EOF) {
        l += print_char(c);
        if (c == '\n') l = 0;
        if (l >= LINE_LENGTH) {
            l = 0;
            printf("\n");
        }
    }
    if (l) printf("\n");
    return 0;
}
