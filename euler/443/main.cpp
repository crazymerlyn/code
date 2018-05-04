#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

vector<long> facs(long n) {
    vector<long> res;
    if (n % 2 == 0) res.push_back(2);
    while (n % 2 == 0) n /= 2;
    for (long i = 3; i * i <= n; i += 2) {
        if (n % i) continue;
        res.push_back(i);
        while (n % i == 0) n /= i;
    }
    if (n > 1) res.push_back(n);
    return res;
}

long gcd(long a, long b) {
    return b ? gcd(b, a % b) : a;
}

long next(long g, long n) {
    long res = 2 * g;
    for (long fac: facs(g-n-1)) {
        res = min(res, n + fac - n % fac);
    }
    return res;
}

int main() {
    long limit = 1e15;
    long n = 4;
    long g = 13;
    while (n <= limit) {
        long k = next(g, n);
        if (k > limit) {
            g += limit - n;
            break;
        }
        g += k - n - 1;
        g += gcd(g, k);
        n = k;
    }
    cout << g << endl;
}


