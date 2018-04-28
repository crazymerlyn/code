from utils import is_prime2 as isprime, fib

def next_prime(n):
    n += 1
    while not isprime(n):
        n += 1
    return n

a = 10 ** 14
A = []
limit = 10 ** 5
for _ in range(limit):
    x = next_prime(a)
    A.append(x)
    a = x

mod = 1234567891011
print(sum(fib(n, mod) for n in A) % mod)
