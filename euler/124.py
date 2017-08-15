from utils import factorize

def product(seq):
    return reduce(lambda x,y:x*y, seq, 1)

limit = 10**5
pos = 10**4

radicals = []

for i in range(1, limit+1):
    radical = product(p for p, _ in factorize(i))
    radicals.append((radical, i))


radicals.sort()
print radicals[pos-1][1]

