from utils import primes

limit = 100

ps = primes(limit)
count = [[0 for _ in ps] for _ in range(limit+1)]

for n in range(1, limit+1):
    for i, p in enumerate(ps):
        if p == n: count[n][i] += 1
        count[n][i] += count[n-p][i]
        if i > 0:
            count[n][i] += count[n][i-1]

for n, cs in enumerate(count):
    if cs[-1] > 5000:
        print n
        break

