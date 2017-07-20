from utils import phi

print max((n for n in xrange(1, 10**6+1)), key=lambda n: 1.0*n / phi(n))
