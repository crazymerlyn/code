#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

vector<long> sieve(long n) {
    vector<long> result;
    vector<bool> isprime(n+1, true);
    for (long i = 2; i <= n; ++i) {
        if (!isprime[i]) continue;
        for (long j = i * i; j <= n; j += i) {
            isprime[j] = false;
        }
    }

    for (long i = 2; i <= n; ++i) {
        if (isprime[i]) result.push_back(i);
    }

    return result;
}

int main() {
    long limit = 5000;
    auto primes = sieve(limit);
    long sum = accumulate(primes.begin(), primes.end(), 0);
    vector<long> count(sum+1, 0);
    count[0] = 1;

    long mod = 1e16;

    long sp = 0;
    for (auto p : primes) {
        sp += p;
        for (long s = sp; s > p - 1; s--) {
            count[s] += count[s-p];
            count[s] %= mod;
        }
    }

    long result = 0;
    for (auto prime: sieve(sum)) {
        result += count[prime];
        result %= mod;
    }

    cout << result << endl;
}

