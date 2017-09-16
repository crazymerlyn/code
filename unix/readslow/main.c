#include <unistd.h>
#include <stdlib.h>
#include <getopt.h>
#include <stdbool.h>
#include <stdio.h>
#include <fcntl.h>
#define SIZE 256

int main(int argc, char **argv) {
    char buf[SIZE];
    int n, c;
    int sleep_time = 3;
    bool seek_to_end = false;
    int fd;

    while ((c = getopt(argc, argv, "en:")) != -1) {
        switch (c) {
        case 'e':
            seek_to_end = true;
            break;
        case 'n':
            sleep_time = atoi(optarg);
            break;
        }
    }

    if (optind < argc) {
        fd = open(argv[optind], 0);
        if (fd == -1) {
            perror(argv[optind]);
            exit(1);
        }

        if (seek_to_end) {
            lseek(fd, 0, SEEK_END);
        }
    }

    for (;;) {
        while ((n = read(fd, buf, sizeof buf)) > 0) {
            write(1, buf, n);
        }
        sleep(sleep_time);
    }
    return 0;
}
