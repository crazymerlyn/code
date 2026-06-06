LIMIT = 15499 / 94744

def phi(n):
    result = n
    p = 2
    temp = n
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1 if p == 2 else 2
    if temp > 1:
        result -= result // temp
    return result

n = 1
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
for p in primes:
    n *= p
    if phi(n) / (n - 1) < LIMIT:
        # backtrack one prime, then multiply by k
        n //= p
        for k in range(2, p):
            candidate = n * k
            if phi(candidate) / (candidate - 1) < LIMIT:
                print(candidate)
                exit()
