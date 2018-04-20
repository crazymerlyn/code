#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int g(int i, int j) {
    int res = 0;
    while (j) {
        res += j;
        j /= i;
    }
    return res;
}

long f(int i, int n) {
    int lo = 1;
    int high = n;
    while (lo != high) {
        int mid = (lo + high) / 2;
        if (g(i, mid) < n) lo = mid + 1 ;
        else high = mid;
    }
    return lo * i;
}

long s(long n) {
    long res = 1;
    long i = 2;
    while (i * i <= n) {
        if (n % i) {
            i += 1; continue;
        }
        int pow = 0;
        while (n % i == 0) {
            pow += 1;
            n /= i;
        }
        res = max(res, f(i, pow));
        i += 1;
    }
    if (n > 1) {
        res = max(res, n);
    }
    return res;
}

int main() {
    int n = 100000000;
    long res = 0;
    for (int i = 2; i <= n; ++i) {
        res += s(i);
    }
    cout << res;
}


