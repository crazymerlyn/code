#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <getopt.h>

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
    int c;
    int reverse = 0;
    while ((c = getopt(argc, argv, "v")) != -1) {
        switch (c) {
        case 'v':
            reverse = 1;
            break;
        default:
            break;
        }
    }
    for (int i = optind; i < argc; i++) {
        FILE* fp = fopen(argv[i], "rb");
        if (fp == NULL) {
            perror(argv[i]);
            continue;
        }
        if (reverse ^ printable(fp)) printf("%s\n", argv[i]);
    }
    return 0;
}
