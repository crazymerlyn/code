from utils import primes, is_prime

ps = list(primes(40))

limit = 10 ** 9

admissible = set()

def make_admissibles(f):
    if f >= limit: return
    if f in admissible: return
    admissible.add(f)
    for p in ps:
        make_admissibles(f * p)
        if f % p: return

make_admissibles(2)
admissible = sorted(admissible)

res = set()
for n in admissible:
    m = 2
    while not is_prime(m + n):
        m += 1
    res.add(m)

print sum(res)
