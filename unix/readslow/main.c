#include <unistd.h>
#include <stdlib.h>
#define SIZE 256

int main(int argc, char **argv) {
    char buf[SIZE];
    int n;
    int sleep_time = 3;

    if (argc > 1 && argv[1][0] == '-') {
        sleep_time = atoi(argv[1] + 1);
    }

    for (;;) {
        while ((n = read(0, buf, sizeof buf)) > 0) {
            write(1, buf, n);
        }
        sleep(sleep_time);
    }
    return 0;
}
