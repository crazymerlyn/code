from itertools import product

def prod(seq):
    return reduce(lambda x,y:x*y, seq)

n = 15
res = 0
for possib in product(*([0, 1] for i in range(n))):
    if sum(possib) > n/2:
        res += prod(1 if x else i+1 for i, x in enumerate(possib))

print prod(range(2, n+2)) / res

