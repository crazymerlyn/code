from utils import is_prime2 as isprime, is_prime, primes
import array

def find_q_s(prime):
    q = prime - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1

    return q, s

def non_residue(prime):
    for z in xrange(prime):
        p = pow(z, (prime - 1) // 2, prime)
        if p == prime -1:
            return z

def find_sq_num(t, prime):
    i = 0
    while t != 1:
        i += 1
        t = t * t % prime
    return i

def calculate_r(p):
    n = (p + 1) / 2
    q, s = find_q_s(p)
    z = non_residue(p)

    m = s
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q + 1) / 2, p)

    while t != 1:
        i = find_sq_num(t, p)
        if i >= m: return
        b = pow(c, 2 ** (m - i - 1), p)
        m = i
        c = b * b % p
        t = t * b * b % p
        r = r * b % p
    yield r
    yield p - r

limit = 5 * 10 ** 7

ps = list(primes(int(2 ** 0.5 * limit)))

els = array.array('B', '1' * (limit + 1))

for p in ps[1:]:
    for r in calculate_r(p):
        init = r if 2 * r * r - 1 != p else r + p
        for k in xrange(init, limit+1, p):
            els[k] = 0

count = 0
for i in xrange(2, limit + 1):
    if els[i]:
        count += 1
print count

