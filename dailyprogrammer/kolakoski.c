#include <stdio.h>
#include <stdint.h>

enum kval { K22, K11, K2, K1 };

void next(enum kval *v) {
    if (*v < 2) {
        *v += 2;
    } else {
        next(v+1);
        *v = !(*v % 2) + 2 * (v[1] % 2);
    }
}

int main() {
    uint64_t n = 1000000000;
    enum kval stack[256] = {0};
    uint64_t counts[2] = {1, 1};
    for (uint64_t i = 2; i < n; ++i) {
        next(stack);
        counts[*stack % 2]++;
    }
    printf("%lu:%lu\n", counts[1], counts[0]);
}
