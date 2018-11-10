#include <bits/stdc++.h>

using namespace std;

bool isprime(long long n) {
    if (n <= 1) return false;
    for (long long i = 2; i * i <= n; ++i) {
        if (n % i == 0) return false;
    }
    return true;
}

vector<long long> divs(long long n) {
    vector<long long> res;
    long long i = 0;
    for (i = 1; i * i < n; ++i) {
        if (n % i == 0) {
            res.push_back(i);
            res.push_back(n / i);
        }
    }
    if (i * i == n) res.push_back(i);
    return res;
}

vector<long long> prime_possibs(long long n) {
    vector<long long> res;
    for (auto p: divs(n)) {
        if (isprime(p + 1)) res.push_back(p + 1);
    }
    sort(res.begin(), res.end(), greater<long long>());
    return res;
}

void func(long long n, vector<long long> &ps, size_t i, vector<long long> &res, long long fac = 1) {
    if (n == 1) {
        res.push_back(fac);
        return;
    }
    if (ps.size() == i) return;
    func(n, ps, i + 1, res, fac);
    if (n % (ps[i] - 1) == 0) {
        fac *= ps[i];
        n /= ps[i] - 1;
        func(n, ps, i + 1, res, fac);
        while (n % ps[i] == 0) {
            fac *= ps[i];
            n /= ps[i];
            func(n, ps, i + 1, res, fac);
        }
    }
}

void phi_possibs(long long n, vector<long long> &res) {
    auto ps = prime_possibs(n);
    func(n, ps, 0, res);
}

int main() {
    long long n; cin >> n;
    vector<long long> res;
    phi_possibs(n, res);
    if (res.size() == 0) {
        cout << 0 << endl;
    } else {
        long long ans = res[0];
        for (auto p: res) ans = min(ans, p);
        cout << ans << endl;
    }
    return 0;
}


