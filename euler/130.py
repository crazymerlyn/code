from utils import primes

ps = list(primes(10**6))
res = 0
count = 0

for n in range(4, 10**6):
    if n in ps: continue
    if n % 2 == 0 or n % 5 == 0: continue
    if count == 25: break

    if pow(10, n-1, 9*n) == 1:
        count += 1
        res += n

print res


