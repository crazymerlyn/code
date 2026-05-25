#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std;

typedef __int128 i128;

long long mul_mod(long long a, long long b, long long m) {
    return (long long)((i128)a * b % m);
}

long long pow_mod(long long a, long long d, long long n) {
    long long r = 1;
    while (d) {
        if (d & 1) r = mul_mod(r, a, n);
        a = mul_mod(a, a, n);
        d >>= 1;
    }
    return r;
}

bool is_prime(long long n) {
    if (n < 2) return false;
    if (n == 2 || n == 3) return true;
    if (n % 2 == 0) return false;
    
    long long d = n - 1;
    int s = 0;
    while (d % 2 == 0) { d /= 2; s++; }
    
    long long bases[] = {2, 3, 5, 7, 11, 13, 17};
    for (long long a : bases) {
        if (a >= n) continue;
        long long x = pow_mod(a, d, n);
        if (x == 1 || x == n - 1) continue;
        bool composite = true;
        for (int r = 0; r < s - 1; r++) {
            x = mul_mod(x, x, n);
            if (x == n - 1) { composite = false; break; }
        }
        if (composite) return false;
    }
    return true;
}

bool prime_proof(long long n) {
    string s = to_string(n);
    int len = s.size();
    for (int i = 0; i < len; i++) {
        char orig = s[i];
        for (char d = '0'; d <= '9'; d++) {
            if (i == 0 && d == '0') continue;
            if (d == orig) continue;
            s[i] = d;
            long long val = stoll(s);
            if (is_prime(val)) return false;
        }
        s[i] = orig;
    }
    return true;
}

bool contains_200(long long x) {
    while (x >= 200) {
        if (x % 1000 == 200) return true;
        x /= 10;
    }
    return false;
}

int main() {
    const long long MAX = 100000000000000LL;
    
    long long max_prime = (long long)sqrt(MAX / 8) + 1;
    
    vector<char> is_p(max_prime + 1, 1);
    vector<long long> primes;
    is_p[0] = is_p[1] = 0;
    for (long long i = 2; i <= max_prime; i++) {
        if (is_p[i]) {
            primes.push_back(i);
            if (i * i <= max_prime) {
                for (long long j = i * i; j <= max_prime; j += i)
                    is_p[j] = 0;
            }
        }
    }
    
    vector<long long> squbes;
    
    for (size_t pi = 0; pi < primes.size(); pi++) {
        long long p = primes[pi];
        long long p2 = p * p;
        if (p2 > MAX / 8) continue;
        
        long long max_q_val = (long long)cbrt((long double)(MAX / p2)) + 1;
        
        for (size_t qj = 0; qj < primes.size() && primes[qj] <= max_q_val; qj++) {
            long long q = primes[qj];
            if (q == p) continue;
            long long q3 = q * q;
            if (q3 > MAX / p2 / q) continue;
            q3 *= q;
            long long val = p2 * q3;
            if (val <= MAX)
                squbes.push_back(val);
        }
    }
    
    sort(squbes.begin(), squbes.end());
    squbes.erase(unique(squbes.begin(), squbes.end()), squbes.end());
    
    int cnt = 0;
    for (long long v : squbes) {
        if (contains_200(v) && prime_proof(v)) {
            cnt++;
            if (cnt == 200) {
                cout << v << endl;
                return 0;
            }
        }
    }
    
    cout << "Only found " << cnt << endl;
    return 0;
}
