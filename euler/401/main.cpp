#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

long gcd(long a, long b) {
    long res = 1;
    if (a % 2 == 0 && b % 2 == 0) res *= 2;
    if (a % 3 == 0 && b % 3 == 0) res *= 3;
    return res;
}

int main() {
    long limit = 1e15;
    long mod = 1e9;
    long res = 0;
    long s = sqrt(limit);
    s %= mod;
    for (long i = 1; i * i <= limit; ++i) {
        long count = limit / i % mod;
        long val = 6;
        long cur = count / gcd(count, val) % mod;
        val /= gcd(count, val);
        cur = cur * (count + 1) / gcd(count + 1, val) % mod;
        val /= gcd(count + 1, val);
        cur = cur * (2*count + 1) / gcd(2*count + 1, val) % mod;
        val /= gcd(2 * count + 1, val);
        res += cur;
        res %= mod;
        res += ((count + mod - s) * i % mod) * i % mod;
        res %= mod;
    }
    cout << res;
}


