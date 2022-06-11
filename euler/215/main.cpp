#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <map>

using namespace std;


vector<unsigned long long> combs(int m) {
    vector<unsigned long long> res;
    if (m < 2) return res;
    if (m < 4) return {1ull << m};
    for (auto x: combs(m - 2)) {
        res.push_back(x + (1ull<<m));
    }
    for (auto x: combs(m - 3)) {
        res.push_back(x + (1ull<<m));
    }
    return res;
}


int main() {
    long long res=0;
    int n = 10;
    int m = 32;
    auto cs = combs(m);
    map<unsigned long long, long long> dp;
    dp[1ull<<m] = 1;

    for (int i = 0; i < n; ++i) {
	cout << i << endl;
        map<unsigned long long, long long> newdp;
	for (auto x: cs) {
            for (auto p: dp) {
                if ((p.first & x) != (1ull<<m)) continue;
                newdp[x] += p.second;
	    }
	}
	dp = newdp;
    }
    for (const auto& p: dp) {
        res += p.second;
    }
    cout << res << endl;
}


