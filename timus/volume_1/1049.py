from collections import defaultdict

def factorize(n):
    res = []
    if n % 2 == 0:
        power = 0
        while n % 2 == 0:
            power += 1
            n //= 2
        res.append((2, power))
    i = 3
    while i * i <= n:
        if n % i == 0:
            power = 0
            while n % i == 0:
                power += 1
                n //= i
            res.append((i, power))
        i += 2
    if n > 1:
        res.append((n, 1))
    return res

res = defaultdict(int)
for _ in range(10):
    n = int(input())
    for p, power in factorize(n):
        res[p] += power

ans = 1
for v in res.values():
    ans = ans * (v + 1) % 10
print(ans)
