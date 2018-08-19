from collections import defaultdict

def factorize(n):
    if n <= 1: return []
    if n % 2 == 0:
        power = 0
        while n % 2 == 0:
            power += 1
            n //= 2
        yield (2, power)
    i = 3
    while i * i <= n:
        if n % i == 0:
            power = 0
            while n % i == 0:
                power += 1
                n //= i
            yield (i, power)
        i += 2
    if n > 1:
        yield (n, 1)

n = int(input())

fs = defaultdict(int)
for prime, power in factorize(n):
    fs[prime] = power

for k in fs:
    if k > 9:
        print(-1)
        exit()

res = []
res.extend([7] * fs[7])
res.extend([5] * fs[5])
res.extend([9] * (fs[3] // 2))
res.extend([8] * (fs[2] // 3))

fs[3] %= 2
fs[2] %= 3
if fs[3] and fs[2]:
    res.extend([6])
    fs[2] -= 1
    fs[3] -= 1
res.extend([3] * fs[3])
if fs[2]:
    res.append(2 ** fs[2])
if not res:
    if n == 1: res = [1]
    else:
        print(10)
        exit()
print("".join(map(str, sorted(res))))
