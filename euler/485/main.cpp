#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <deque>

using namespace std;

int main() {
    int n = 100000000;
    int m = 100000;
    vector<bool> isprime(n+1, true);
    vector<short> factors(n+1, 1);
    for (int i = 2; i <= n; ++i) {
        if (not isprime[i]) continue;
        for (long j = (long)i*i; j <= n; j += i) isprime[j] = false;
        for (long j = i; j <= n; j += i) {
            int k = j;
            int p = 0;
            while (k % i == 0) {
                k /= i;
                p += 1;
            }
            factors[j] *= (p + 1);
        }
    }

    deque<pair<int,int>> window;
    for (int i = 1; i <= m; ++i) {
        while (window.size() && window.back().second <= factors[i]) {
            window.pop_back();
        }
        window.push_back({i, factors[i]});
    }

    long res = window.front().second;
    for (int i = m+1; i <= n; ++i) {
        while (window.size() && window.back().second <= factors[i]) {
            window.pop_back();
        }
        window.push_back({i, factors[i]});
        if (window.front().first <= i - m) window.pop_front();
        res += window.front().second;
    }
    cout << res << endl;
}


