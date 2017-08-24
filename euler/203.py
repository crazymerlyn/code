from utils import factorize
from math import factorial

def is_sq_free(n, k):
    """Checks whether C(n, k) is square free)"""
    from collections import Counter
    c = Counter()
    for i in range(1, k+1):
        c += Counter(dict(factorize(n - i + 1)))
        c -= Counter(dict(factorize(i)))
    return all(v == 1 for v in c.values())

res = set()
for i in range(51):
    for j in range(i+1):
        if is_sq_free(i, j):
            res.add(factorial(i) / factorial(i - j) / factorial(j))
print sum(res)
