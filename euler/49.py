def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

from collections import Counter

counts = Counter()
for a in range(1000, 10000):
    if is_prime(a):
        b = a + 3330
        c = a + 6660
        if c < 10000 and is_prime(b) and is_prime(c):
            if Counter(str(a)) == Counter(str(b)) == Counter(str(c)):
                print(str(a) + str(b) + str(c))
