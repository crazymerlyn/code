#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <map>

using namespace std;

long limit = 4e7;
vector<long> totient(limit+1, 0);

long chain(long n) {
    static map<long, long> cache;

    if (cache.find(n) == cache.end()) {
        if (n == 1) cache[n] = 1;
        else cache[n] = 1 + chain(totient[n]);
    }
    return cache[n];
}

int main() {
    vector<bool> isprime(limit+1, true);
    long result = 0;

    for (long i = 1; i <= limit; ++i)
        totient[i] = i;

    for (long i = 2; i <= limit; ++i) {
        if (not isprime[i]) continue;
        for (long j = i * i; j <= limit; j += i) {
            isprime[j] = false;
        }
        for (long j = i; j <= limit; j += i) {
            totient[j] = totient[j] * (i - 1) / i;
        }
    }

    vector<long> primes;
    for (long i = 2; i<=limit; ++i) {
        if (isprime[i]) primes.push_back(i);
    }

    for (auto prime : primes) {
        if (chain(prime) == 25) {
            result += prime;
        }
    }

    cout << result << endl;
}

