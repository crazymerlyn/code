#include <bits/stdc++.h>

using namespace std;

int main() {
    int limit = 1e6;
    vector<long double> sf(limit + 1);
    for (int i = 1; i <= limit; ++i) {
        for (int j = i; j <= limit; j += i) {
            sf[j] += i;
        }
        sf[i] /= i;
    }
    int i, j; cin >> i >> j;
    int res = -1;
    long double min_triv = 1e8;
    for (int n = i; n <= j; ++n) {
        if (sf[n] <= min_triv) {
            min_triv = sf[n];
            res = n;
        }
    }
    cout << res << endl;
    return 0;
}


