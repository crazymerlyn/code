from collections import defaultdict

def factorize(n):
    res = defaultdict(int)
    if n < 2: return res
    if n % 2 == 0:
        power = 0
        while n % 2 == 0:
            power += 1
            n //= 2
        res[2] = power
    i = 3
    while i * i <= n:
        if n % i == 0:
            power = 0
            while n % i == 0:
                power += 1
                n //= i
            res[i] = power
        i += 2
    if n > 1:
        res[n] = 1
    return res

fs = [factorize(i) for i in range(50001)]

m, n = [int(x) for x in input().split()]

if n * 2 > m: n = m - n
res = defaultdict(int)
for i in range(1, n+1):
    for k, v in fs[m - n + i].items():
        res[k] += v
    for k, v in fs[i].items():
        res[k] -= v

print(sum(1 for k in res if res[k] > 0))
