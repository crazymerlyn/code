#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

long gcd(long a, long b) {
    return b ? gcd(b, a % b) : a;
}

int main() {
    long res = 0;
    long m = 100;
    long gcd_table[m + 1][m + 1];
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= m; j++) {
            gcd_table[i][j] = gcd(i, j);
        }
    }
    vector<bool> is_square(4 * m * m + 4 * m + 1, false);
    for (int i = 1; i * i < is_square.size(); ++i) {
        is_square[i * i] = true;
    }
    for (int a = 2; a <= m+1; ++a) {
        for (int b = 2; b <= m+1; ++b) {
            for (int c = 2; c <= m+1; ++c) {
                for (int d = 2; d <= m+1; ++d) {
                    int lattice = 0;
                    lattice += (a * b - gcd_table[a-1][b-1] - 1) / 2;
                    lattice += (b * c - gcd_table[b-1][c-1] - 1) / 2;
                    lattice += (c * d - gcd_table[c-1][d-1] - 1) / 2;
                    lattice += (d * a - gcd_table[d-1][a-1] - 1) / 2;
                    lattice -= (a + b + c + d) - 5;
                    if (is_square[lattice]) res += 1;
                }
            }
        }
    }
    cout << res << endl;
}


