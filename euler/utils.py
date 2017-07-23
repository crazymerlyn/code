def primes(n):
    isprime = [True for _ in range(n+1)]
    for i in range(2, n+1):
        if not isprime[i]: continue
        for j in range(i*i, n+1, i):
            isprime[j] = False

    res = []
    for i in range(2, n+1):
        if isprime[i]: res.append(i)

    return res

def factorize(n):
    res = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            power = 0
            while n % i == 0:
                power += 1
                n //= i
            res.append((i, power))
        i += 1
    if n > 1:
        res.append((n, 1))
    return res

def phi(n):
    res = 1
    for prime, power in factorize(n):
        res *= prime ** power - prime ** (power-1)
    return res

def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5)+1))

