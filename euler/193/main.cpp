#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    long limit = 1l << 50;
    long N = sqrt(limit);

    vector<bool> ign(N + 1, 0);
    vector<bool> pos(N + 1, 1);
    vector<bool> prime(N + 1, 1);

    for (long i = 2; i <= N; ++i) {
        if (!prime[i]) continue;
        for (long j = i; j <= N; j += i) {
            pos[j] = !pos[j];
        }
        for (long j = i*i; j <= N; j += i) {
            prime[j] = false;
        }
        for (long j = i*i; j <= N; j += i*i) {
            ign[j] = 1;
        }
    }


    long res = 0;
    for (int i = 1; i <= N; i++) {
        if (ign[i]) continue;
        if (pos[i]) res += limit / i / i;
        else res -= limit / i / i;
    }

    cout << res << endl;
}

