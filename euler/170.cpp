#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int PAND = (1 << 10) - 1;

int digits_mask(long long x) {
    int m = 0;
    while (x) {
        m |= 1 << (x % 10);
        x /= 10;
    }
    return m;
}

int digit_count(long long x) {
    if (x == 0) return 1;
    int c = 0;
    while (x) { c++; x /= 10; }
    return c;
}

int main() {
    long long best = 0;
    string digits = "0123456789";
    do {
        if (digits[0] == '0') continue;
        string s = digits;
        for (int n_len = 1; n_len <= 8; n_len++) {
            if (s[n_len] == '0') continue;
            long long n = stoll(s.substr(0, n_len));
            for (int a_len = 1; a_len <= 9 - n_len; a_len++) {
                if (s[n_len + a_len] == '0') continue;
                int b_len = 10 - n_len - a_len;
                if (b_len < 1) continue;
                
                long long a = stoll(s.substr(n_len, a_len));
                long long b = stoll(s.substr(n_len + a_len));
                
                long long p1 = n * a;
                long long p2 = n * b;
                
                int d1 = digit_count(p1);
                int d2 = digit_count(p2);
                if (d1 + d2 != 10) continue;
                
                int mask = digits_mask(p1) | digits_mask(p2);
                if (mask == PAND) {
                    long long val = stoll(to_string(p1) + to_string(p2));
                    if (val > best) best = val;
                }
            }
        }
    } while (next_permutation(digits.begin(), digits.end()));
    
    cout << best << endl;
    return 0;
}
