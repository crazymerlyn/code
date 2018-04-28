#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
    long q = 10000000;
    long mod = 50515093;
    long s = 290797;
    long res = 0;
    long p = 61;

    long mod2 = 713342911662882601; // 61 ^ 10
    long pp = 1;
    long spp = 0;
    long t = 0;
    for (int i = 1; i <= q; ++i) {
        s = s * s % mod;
        t = s % p;

        spp += pp;
        spp %= mod2;

        pp *= p;
        pp %= mod2;

        res += spp * t;
        res %= mod2;
    }
    cout << res << endl;
}


