from utils import primes

limit = 5 * 10**7
ps = primes(int(limit**0.5))

sqs = [p*p for p in ps if p*p < limit]
cubes = [p**3 for p in ps if p**3 < limit]
quads = [p**4 for p in ps if p**4 < limit]

res = set()
for sq in sqs:
    for cube in cubes:
        if sq + cube > limit: break
        for quad in quads:
            n = sq+cube+quad
            if n >= limit: break
            res.add(n)
print(len(res))
