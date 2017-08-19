from utils import primes

limit = 4 * 10 ** 6 * 2 - 1

ps = list(primes(1000))[:15]
m = float('inf')

def minimum(i, plimit, val, n):
    global m
    for j in range(1, plimit+1):
        if n * ps[i] ** j > m: break
        if val * (2*j + 1) > limit:
            if n * ps[i] ** j < m:
                m = n * ps[i] ** j
        else:
            minimum(i+1, j, val * (2 * j + 1), n * ps[i] ** j)

minimum(0, 20, 1, 1)
print m

