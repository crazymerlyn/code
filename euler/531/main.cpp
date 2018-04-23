#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

// C function for extended Euclidean Algorithm
int gcdExtended(int a, int b, long *x, long *y);
 
// Function to find modulo inverse of a
long modInverse(long a, long m)
{
    long x, y;
    int g = gcdExtended(a, m, &x, &y);
    return (x%m + m) % m;
}
 
// C function for extended Euclidean Algorithm
int gcdExtended(int a, int b, long *x, long *y)
{
    // Base Case
    if (a == 0)
    {
        *x = 0, *y = 1;
        return b;
    }
 
    long x1, y1; // To store results of recursive call
    int gcd = gcdExtended(b%a, a, &x1, &y1);
 
    // Update x and y using results of recursive
    // call
    *x = y1 - (b/a) * x1;
    *y = x1;
 
    return gcd;
}


long phi(long n) {
    long res = n;
    for (int i = 2; i * i <= n; ++i) {
        if (n % i) continue;
        res -= res / i;
        while (n % i == 0) n /= i;
    }
    if (n > 1)
        res -= res / n;
    return res;
}

long gcd(long a, long b) {
    return b ? gcd(b, a % b) : a;
}

long func(long a, long n, long b, long m) {
    long g = gcd(n, m);
    if ((b - a) % g) return 0;

    m /= g;
    n /= g;

    return (m * n*g + (a + (b - a) / g * modInverse(n, m) * n * g) % (m * n * g)) % (m*n*g);
}
int main() {
    int l = 1000000;
    int h = 1005000;
    vector<long> phis;

    for (int i = l; i <= h; ++i) {
        phis.push_back(phi(i));
    }

    long ans = 0;
    for (int n = l; n < h; ++n) {
        for (int m = n + 1; m < h; ++m) {
            ans += func(phis[n-l], n, phis[m-l], m);
        }
    }
    cout << ans << endl;
}


