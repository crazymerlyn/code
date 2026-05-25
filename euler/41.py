def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

from itertools import permutations
digits = '123456789'
for l in range(9, 0, -1):
    best = 0
    for p in permutations(digits[:l]):
        n = int(''.join(p))
        if n > best and is_prime(n):
            best = n
    if best:
        print(best)
        break
