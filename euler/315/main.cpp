#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int mapping[] = {0b1110111, 0b0010010, 0b1011101, 0b1011011, 0b0111010,
                 0b1101011, 0b1101111, 0b1110010, 0b1111111, 0b1111011};

int cost[128];

vector<int> sieve(int n, int m) {
    vector<bool> isprime(m+1, true);

    for (int i = 2; i * i <= m; ++i) {
        if (not isprime[i]) continue;
        for (int j = i * i; j <= m; j += i) {
            isprime[j] = false;
        }
    }

    vector<int> res;
    for (int i = n; i <= m; ++i) {
        if (isprime[i]) res.push_back(i);
    }
    return res;
}

int root(int n) {
    int res = 0;
    while (n) {
        res += n % 10;
        n /= 10;
    }
    return res;
}

int sum_digits(int n) {
    int res = 0;
    while (n) {
        res += n % 10;
        n /= 10;
    }
    return res;
}

int get_cost(int n) {
    int res = 0;
    while (n) {
        res += cost[mapping[n % 10]];
        n /= 10;
    }
    return res;
}

int cost_diff(int n, int newn) {
    int res = 0;
    while (n) {
        if (newn)
            res += cost[mapping[n % 10] ^ mapping[newn % 10]];
        else
            res += cost[mapping[n % 10]];
        n /= 10;
        newn /= 10;
    }
    return res;
}

int sam(int n) {
    int res = 0;
    while (n >= 10) {
        res += get_cost(n) * 2;
        n = sum_digits(n);
    }
    if (n) res += get_cost(n) * 2;
    return res;
}

int maxx(int n) {
    int temp = n;
    int res = 0;
    int newn = 0;
    while (temp) {
        res += cost[mapping[temp % 10]];
        newn += temp % 10;
        temp /= 10;
    }
    while (newn != n) {
        res += cost_diff(n, newn);
        int temp = newn;
        newn = sum_digits(newn);
        n = temp;
    }

    res += get_cost(n);
    return res;
}

int main() {
    for (int i = 0; i <= mapping[8]; ++i) {
        cost[i] = __builtin_popcount(i);
    }
    auto primes = sieve(1e7, 2e7);
    long res = 0;

    for (auto prime: primes) {
        res += sam(prime) - maxx(prime);
    }

    cout << res << endl;
}


