from utils import primes

res = 0
for p in primes(10**8):
    if p < 5: continue
    res += (p - 3) * pow(8, p-2, p) % p

print res

