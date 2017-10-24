#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
    long res = 0;

    for (int sum = 0; sum <= 36; ++sum) {
        for (int a = 0; a <= 9; a++) {
            for (int b = 0; b <= min(9 , sum - a); b++) {
                for (int c = 0; c <= min(9, sum - a - b); c++) {
                    int d = sum - a - b - c;
                    if (d > 9) continue;
                    for (int e = 0; e <= min(9, sum - a); ++e) {
                        for (int f = 0; f <= min(9, sum - e); f++) {
                            for (int g = 0; g <= min(9, sum - e -f); ++g) {
                                int h = sum - e - f - g;
                                if (h > 9) continue;
                                for (int i = 0; i <= min(9, sum - a - e); ++i) {
                                    int m = sum - a - e - i;
                                    int j = sum - d - g - m;
                                    int n = sum - b - f - j;

                                    if (m > 9 || j > 9 || n > 9 || n < 0 || j < 0) continue;
                                    for (int k = 0; k <= min(9, sum - i - j); ++k) {
                                        int l = sum - i - j - k;
                                        int o = sum - c - g - k;
                                        int p = sum - d - h - l;
                                        if (sum == a + f + k + p && l <= 9 && o <= 9 && p <= 9 && o >= 0 && p >= 0) res += 1;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    cout << res << endl;
}


