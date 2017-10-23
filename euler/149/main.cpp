#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

long max_seq(const vector<long> & ar) {
    long res = 0;
    long cur = 0;
    for (auto elem: ar) {
        cur = max(elem, cur + elem);
        res = max(res, cur);
    }
    return res;
}

int main() {
    long n = 2000;
    vector<vector<long>> mat(n, vector<long>(n));
    long mod = 1000000;

    for (long i = 0; i < 55; ++i) {
        long k = i + 1;
        mat[0][i] = (100003 - 200003 * k + 300007 * k * k * k) % mod - 500000;
    }

    for (long in = 55; in < n * n; ++in) {
        long i = in / n, j = in % n;
        long i2 = (in - 24) / n, j2 = (in - 24) % n;
        long i3 = (in - 55) / n, j3 = (in - 55) % n;

        mat[i][j] = (mat[i2][j2] + mat[i3][j3] + mod) % mod - 500000;
    }

    long res = 0;

    //rows
    for (int i = 0; i < n; i++) {
        res = max(res, max_seq(mat[i]));
    }

    //columns
    for (int j = 0; j < n; j++) {
        long cur = 0;
        for (int i = 0; i < n; i++) {
            cur = max(mat[i][j], cur + mat[i][j]);
            res = max(res, cur);
        }
    }

    //diagonals
    for (int k = 0; k < n; k++) {
        long cur = 0;
        for (int i = 0, j = k; j < n; i++, j++) {
            cur = max(mat[i][j], cur + mat[i][j]);
            res = max(res, cur);
        }
        cur = 0;
        for (int i = 0, j = k; j >= 0; i++, j--) {
            cur = max(mat[i][j], cur + mat[i][j]);
            res = max(res, cur);
        }
        cur = 0;
        for (int i = k, j = 0; i < n; i++, j++) {
            cur = max(mat[i][j], cur + mat[i][j]);
            res = max(res, cur);
        }
        cur = 0;
        for (int i = k, j = n-1; i < n; i++, j--) {
            cur = max(mat[i][j], cur + mat[i][j]);
            res = max(res, cur);
        }
    }

    cout << res << endl;
}


