from utils import primes, modinv

limit = 1000000

ps = list(primes(limit + 100))[2:]

res = 0
for p1, p2 in zip(ps, ps[1:]):
    if p1 > limit: break
    power10 = 10 ** len(str(p1))
    res += ((p2 - p1) * modinv(power10, p2) % p2) * power10 + p1
print res

