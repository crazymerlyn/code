from utils import primes2, is_prime2, is_prime

def is_prime_gen(n):
    for d in range(1, int(n**0.5)+1):
        if not n % d == 0: continue
        s = d + n // d
        if s not in ps:
            return False
    return True

ps = set()
limit = 10**8
for p in primes2():
    if p < limit: ps.add(p)
    else: break

s = 0
for p in ps:
    if p % 4 != 3: continue
    n = p - 1
    if is_prime_gen(n): s += n

print s
