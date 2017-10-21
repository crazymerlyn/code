from utils import primes

def f(n, k):
    res = 0
    while n:
        res += n // k
        n //= k
    return res * k

n = 20000000
k = 15000000

res = 0
for p in primes(n):
    res += f(n, p) - f(k , p) - f(n - k, p)

print(res)

