from math import factorial

def comb(n, r):
    return factorial(n) / factorial(n-r) / factorial(r)

k, m, n = map(int, raw_input().split())

total = comb(k + m + n, 2)

pos = 0

pos += k * (m + n) + k * (k - 1) / 2

pos += m * n / 2.0 + m * (m - 1) / 2 * 0.75

print pos / total
