def is_square(n):
    return int(round(n**0.5))**2 == n

def mat_mul(a, b):
    res = [[0 for _ in b[0]] for _ in a]
    for i in range(len(a)):
        for j in range(len(b[0])):
            res[i][j] = sum(a[i][k] * b[k][j] for k in range(len(b)))
    return res

def fib(n):
    a = [[1, 1], [1, 0]]
    res = [[1, 0], [0, 1]]
    while n:
        if n % 2:
            res = mat_mul(res, a)
        a = mat_mul(a, a)
        n //= 2
    return res[0][1]

def primes(n):
    isprime = [True for _ in range(n+1)]
    for i in range(2, n+1):
        if not isprime[i]: continue
        for j in range(i*i, n+1, i):
            isprime[j] = False

    res = []
    for i in range(2, n+1):
        if isprime[i]: res.append(i)

    return res

def factorize(n):
    res = []
    if n % 2 == 0:
        power = 0
        while n % 2 == 0:
            power += 1
            n //= 2
        res.append((2, power))
    i = 3
    while i * i <= n:
        if n % i == 0:
            power = 0
            while n % i == 0:
                power += 1
                n //= i
            res.append((i, power))
        i += 2
    if n > 1:
        res.append((n, 1))
    return res

def phi(n):
    res = 1
    for prime, power in factorize(n):
        res *= prime ** power - prime ** (power-1)
    return res

def is_prime(n):
    return n > 1 and all(n % i for i in xrange(2, int(n**0.5)+1))

def is_prime2(n):
    import random
    if n < 2: return False
    for i in range(10):
        a = random.randint(1, n-1)
        if pow(a, n-1, n) != 1:
            return False
    return True

def decimal_to_roman(n):
    roman = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
    }
    res = ""
    for d in sorted(roman.keys(), reverse=True):
        if d > n: continue
        res += roman[d] * (n // d)
        n %= d
    return res

def roman_to_decimal(s):
    decimal = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    last = 0
    n = 0
    for c in s:
        d = decimal[c]
        if d > last:
            n -= 2 * last
        n += d
        last = d
    return n

wheel = [2,4,2,4,6,2,6,4,2,4,6,6,2,6,4,2,6,4,6,8,4,2,4,2,
         4,8,6,4,6,2,4,6,2,6,6,4,2,4,6,2,6,4,2,4,2,10,2,10]
wsize = 48

def primes2():
    for x in (2, 3, 5, 7): yield x
    for x in wsieve(): yield x

def wsieve():       # wheel-sieve, by Will Ness. cf. ideone.com/WFv4f
    yield 11        # cf. https://stackoverflow.com/a/10733621/849891
    mults = {}      #     https://stackoverflow.com/a/19391111/849891
    ps = wsieve()
    p = next(ps)
    psq, c, i = p*p, 11, 0                   # 13 = 11 + wheel[0]
    cbase, ibase = 11, 0
    while True:
        c += wheel[i] ; i = (i+1) % wsize    # 17 = 13 + wheel[1]
        if c in mults:
            (j,pbase) = mults.pop(c)         # add(mults, NEXT c, j, pbase)
        elif c < psq:
            yield c ; continue
        else:          # (c==psq)
            while not cbase == p:
                cbase += wheel[ibase]
                ibase = (ibase+1) % wsize    # ibase - initial offset into wheel, for p
            j, pbase = ibase, p              # add(mults, NEXT c, ibase, p)
            p = next(ps) ; psq = p*p
        m = c + pbase*wheel[j] ; j = (j+1) % wsize    # mults(p) = map (*p)
        while m in mults:                             #              roll(wheel,ibase,p)
            m += pbase*wheel[j] ; j = (j+1) % wsize
        mults[m] = (j,pbase)
