#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;


long fibonacci(int n) {
    long a = 0, b = 1;
    for (int i = 1; i <= n; ++i) {
        b = a + b;
        a = b - a;
    }
    return a;
}


int main() {
    long n = fibonacci(44);
    vector<int> primes;
    vector<bool> notprime(n + 1);

    for (long i = 3; i*i <= n; i += 2) {
        if (notprime[i]) continue;
        for (long j = i * i; j <= n; j += i + i) notprime[j] = true;
    }

    primes.push_back(2);
    for (int i = 3; i <= n; i += 2) {
        if (not notprime[i]) primes.push_back(i);
    }

    vector<long> fibs;
    for (int k = 3; k <= 44; k++) fibs.push_back(fibonacci(k));

    long res = 0;
    for (auto fib: fibs) {
        res += upper_bound(primes.begin(), primes.end(), fib) - primes.begin();
        res += upper_bound(primes.begin(), primes.end(), fib-2) - primes.begin();
        res += max(fib - 4, 0l) / 2;
        long count = max(fib / 2 - 2, 0l);
        res += count * ((fib + 1) / 2 - 2);
    }
    
    cout << res << endl;
}


