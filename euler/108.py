from utils import factorize, product

for n in xrange(2, 1000000):
    c = product(2*p + 1 for prime, p in factorize(n))
    if c > 1999:
        print n
        break

