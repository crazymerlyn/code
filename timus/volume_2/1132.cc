#include <bits/stdc++.h>

using namespace std;

long long pow(long long a, long long b, long long m) {
    long long res = 1;
    while (b) {
        if (b % 2) res = res * a % m;
        a = a * a % m;
        b /= 2;
    }
    return res;
}

int non_residue(int p) {
    for (int i = 2; i < p; ++i) {
        if (pow(i, (p-1)/2, p) != 1) return i;
    }
}

int root(int n, int p) {
    int q = p - 1;
    int s = 0;
    while (q % 2 == 0) {
        q /= 2;
        s += 1;
    }
    int z = non_residue(p);
    int m = s;
    int c = pow(z, q, p);
    int t = pow(n, q, p);
    int r = pow(n, (q + 1) / 2, p);

    while (t != 1) {
        int i = 0;
        for (int t_temp = t; t_temp != 1; t_temp = t_temp * t_temp % p) i += 1;
        int b = pow(c, 1 << (m - i - 1), p);
        m = i;
        c = b * b % p;
        t = t * c % p;
        r = r * b % p;
    }

    return min(r, p - r);
}

int main(int argc, const char *argv[])
{
    int test_cases;
    cin >> test_cases;
    while(test_cases--) {
        int a, n;
        cin >> a >> n;
        if (n <= 2) cout << a % n << endl;
        else if (pow(a, (n - 1) / 2, n) == 1) {
            int r = root(a, n);
            cout << r << " " << n - r << endl;
        } else {
            cout << "No root" << endl;
        }
    }
    return 0;
}
