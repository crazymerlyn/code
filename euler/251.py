from itertools import product
from utils import factorize
from functools import reduce
from operator import mul

# The problem can be parametrized with a = 3k + 2.
# The equation becomes b^2 * c = (k+1)^2 * (8k + 5)

def all_factors(fs):
    for fs in product(*[[x**i for i in range(y+1)] for x,y in fs]):
        yield reduce(mul, fs, 1)

limit = 11*10**7
count = 0
for k in range((limit - 2) // 3):
    v = (k+1) ** 2 * (8*k + 5)
    fs = dict((x, y*2) for x,y in factorize(k+1))
    for x,y in factorize(8*k+5):
        fs[x] = fs.get(x,0) + y
    fs = [(x, y//2) for x,y in fs.items() if y > 1]

    for b in all_factors(fs):
        c = v // (b*b)
        if 3*k + 2 + b + c <= limit:
            count += 1

print(count)
