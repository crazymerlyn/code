#include <bits/stdc++.h>

using namespace std;

int main() {
    int n; cin >> n;
    n *= 2;
    int res = 1;
    for (int i = 2; i * i < n; ++i) {
        if (n % i == 0 && (n / i - i) % 2 == 1) res = i;
    }

    int p = res;
    int a = (n / p - p + 1) / 2;

    cout << a << " " << p << endl;
    return 0;
}


