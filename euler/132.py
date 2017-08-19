from utils import primes

ps = primes(10**6)

limit = 10 ** 9
n = 40
res = 0

for p in ps:
    if not n: break
    if pow(10, 10**9, 9*p) == 1:
        n -= 1
        res += p

print res

