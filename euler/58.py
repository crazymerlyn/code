def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

primes = 0
total = 1
for layer in range(1, 100000):
    for corner in range(4):
        n = (2*layer + 1)**2 - 2*layer*corner
        if is_prime(n):
            primes += 1
    total += 4
    if total > 0 and primes * 10 < total:
        print(2*layer + 1)
        break
