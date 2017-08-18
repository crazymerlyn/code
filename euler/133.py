from utils import primes

def factor_count(n):
    a, b = 0, 0
    while n % 2 == 0:
        n //= 2
        a += 1

    while n % 5 == 0:
        n //= 5
        b += 1

    return a, b

limit = 10**5
res = 0

for prime in primes(limit):
    a, b = factor_count(prime - 1)
    possib = False
    for i in range(a+1):
        for j in range(b+1):
            if i == 0 and j == 0: continue
            if pow(10, 2**i*5**j, 9*prime) == 1:
                possib = True
                break
        if possib: break

    if not possib:
        res += prime
print res

