#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

long phi(long n) {
    long res = n;
    for (int i = 2; i * i <= n; i++) {
        if (n % i) continue;
        res -= res / i;
        while (n % i == 0) n /= i;
    }
    if (n > 1) res -= res / n;
    return res;
}

int main() {
    long limit = 5e8;
    vector<bool> isprime(limit+1, true);
    vector<bool> hassq(limit+1, false);
    vector<bool> mobius(limit+1, false);

    for (long i = 2; i <= limit; ++i) {
        if (not isprime[i]) continue;

        for (long j = i * i; j <= limit; j += i) {
            isprime[j] = false;
        }
        for (long j = i; j <= limit; j += i) {
            if (j % (i * i) == 0) hassq[j] = true;
            mobius[j] = !mobius[j];
        }
    }

    long res = 1;
    for (long i = 1; i <= limit; i++) {
        if (not hassq[i]) 
            res += (mobius[i] ? -1 : 1) * (limit / i) * (limit / i);
    }
    limit /= 2;
    while (limit) {
        res -= 1;
        for (long i = 1; i <= limit; ++i) {
            if (not hassq[i]) {
                res -= (mobius[i] ? -1 : 1) * (limit / i) * (limit / i);
            }
        }
        limit /= 2;
    }
    cout << res / 2 << endl;
}


