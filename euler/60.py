from utils import primes, is_prime as isprime
from collections import defaultdict

ps = primes(10**4)[1:]

concatenable = {p: set() for p in ps}

n = len(ps)

for p in ps:
    for q in ps:
        if isprime(int(str(p) + str(q))):
            concatenable[p].add(q)

for p in ps:
    for q in concatenable[p]:
        if q <= p: continue
        if p not in concatenable[q]: continue
        for r in concatenable[p] & concatenable[q]:
            if r <= q: continue
            if p not in concatenable[r] or q not in concatenable[r]: continue
            for s in concatenable[p] & concatenable[q] & concatenable[r]:
                if s <= r: continue
                if p not in concatenable[s] or q not in concatenable[s] or r not in concatenable[s]: continue
                for t in concatenable[p] & concatenable[q] & concatenable[r] & concatenable[s]:
                    if t <= s: continue
                    if set([p, q, r, s]) <= concatenable[t]:
                        print p, q, r, s, t, p + q + r + s + t

