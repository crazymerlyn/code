#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

long pow(long a, long b, long m) {
    a %= m;
    long res = 1;
    while (b) {
        if (b % 2) res = res * a % m;
        a = a * a % m;
        b /= 2;
    }
    return res;
}

vector<long> prime_sieve(long limit) {
    vector<bool> isprime(limit+1, true);
    for (long i = 2; i <= limit; ++i) {
        if (!isprime[i]) continue;
        for (long j = i * i; j <= limit; j += i) {
            isprime[j] = false;
        }
    }
    vector<long> res;
    for (long i = 2; i <= limit; ++i) {
        if (isprime[i]) res.push_back(i);
    }
    return res;
}

long max_pow(long a, long b) {
    long res = 0;
    while (a) {
        a /= b;
        res += a;
    }
    return res;
}

int main() {
    long limit = 100000000;
    auto primes = prime_sieve(limit);
    long res = 1;
    long mod = 1000000009;
    for (auto prime: primes) {
        auto p = max_pow(limit, prime) * 2;
        res *= (1 + pow(prime, p, mod));
        res %= mod;
    }
    cout << res << endl;
}


