#include <stdio.h>
#include <ctype.h>

int main() {
    int c;
    while ((c = getchar()) != EOF) {
        if (isprint(c) || c == '\t' || c == '\n') putchar(c);
        else printf("0x%x", c);
    }
    return 0;
}
