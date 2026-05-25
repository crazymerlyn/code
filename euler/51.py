def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

from itertools import combinations

limit = 1000000
is_prime_arr = [True] * limit
for i in range(2, int(limit ** 0.5) + 1):
    if is_prime_arr[i]:
        step = i
        start = i * i
        is_prime_arr[start:limit:step] = [False] * ((limit - 1 - start) // step + 1)

primes = [i for i in range(2, limit) if is_prime_arr[i]]
prime_set = set(primes)

for p in primes:
    s = str(p)
    l = len(s)
    for r in range(1, l):
        for positions in combinations(range(l), r):
            count = 0
            first = None
            for d in range(10):
                if d == 0 and 0 in positions:
                    continue
                lst = list(s)
                for pos in positions:
                    lst[pos] = str(d)
                m = int(''.join(lst))
                if m in prime_set:
                    count += 1
                    if first is None:
                        first = m
            if count == 8:
                print(first)
                exit()
