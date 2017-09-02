from utils import is_prime2 as isprime, primes

def calc_mods(p):
    res = []
    for i in range(p):
        j = i * i % p
        for off in (1, 3, 7, 9, 13, 27):
            if (j + off) % p == 0:
                break
        else:
            res.append(i)
    return res

limit = 15 * 10 ** 7
res = 0

mods = {p:calc_mods(p) for p in primes(500)}

for n in xrange(0, limit+1, 210):
    for off in (10, 80, 130, 200):
        k = n + off
        possib = True
        for p in mods:
            if k * k > p and k % p not in mods[p]:
                possib = False
                break
        if not possib: continue
        k = (n + off) ** 2
        ps = []
        for j in range(k+1, k+28, 2):
            if isprime(j):
                ps.append(j)
        if ps == [k+1, k+3, k+7, k+9, k+13, k+27]:
            res += n + off

print res

