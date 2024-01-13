from math import gcd
from utils import factorize
from itertools import product
from functools import reduce
import operator

def fib(n):
    a,b=0,1
    for _ in range(n):
        a,b = b, a+b
    return a


period = 120
limit = 10**9

fibs = [fib(i) for i in range(period+2)]
def get_period(val):
    for i in range(1, period+1):
        if fibs[i]%val == fibs[0] and fibs[i+1]%val == fibs[1]:
            return i

res = 0
d = gcd(fib(period), fib(period+1)-1)
for fac in product(*[[f**x for x in range(p+1)] for f,p in factorize(d)]):
    val = reduce(operator.mul, fac, 1)
    if val <= limit and get_period(val) == period:
        res += val
print(res)

