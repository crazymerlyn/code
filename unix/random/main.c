#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main(int argc, char **argv) {
    FILE *fp = stdin;
    if (argc > 1) {
        fp = fopen(argv[1], "r");
        if (!fp) {
            perror(argv[1]);
            exit(1);
        }
    }

    char line[256];
    int chance = 1;
    char ans[256] = "";
    srand(time(0));

    while (fgets(line, sizeof line, fp)) {
        if (rand() % chance == 0) {
            strcpy(ans, line);
        }
        chance += 1;
    }

    printf("%s", ans);

    return 0;
}
