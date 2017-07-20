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

