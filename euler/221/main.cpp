#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>

using namespace std;

int main() {
    long limit = 160000;
    set<long> ans;
    for (long p = 1; p <= limit; ++p) {
        long i;
        long n = 1 + p * p;
        long newlimit = min(p, limit - p);
        for (i = 1; i <= newlimit; ++i) {
            if (n % i) continue;
            long q = p + i;
            long r = p + n / i;
            if (q * r > 1000000000000000000ll/p) continue;
            ans.insert(p * q * r);
        }
    }
    vector<long> res(ans.begin(), ans.end());
    sort(res.begin(), res.end());
    cout << res[149999] << endl;
}


