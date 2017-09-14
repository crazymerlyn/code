#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int printable(FILE* fp) {
    int c;
    while ((c = getc(fp)) != EOF) {
        if (!isprint(c) && c != '\t' && c != '\n' && c != '\r') { 
            return 0;
        }
    }
    return 1;
}

int main(int argc, char **argv) {
    for (int i = 1; i < argc; i++) {
        FILE* fp = fopen(argv[i], "rb");
        if (printable(fp)) printf("%s\n", argv[i]);
    }
    return 0;
}
