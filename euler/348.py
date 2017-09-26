from collections import Counter

def palindromic(n):
    return n == int(str(n)[::-1])

limit = 9 * 10 ** 8
sqs = [x * x for x in xrange(1, int(limit ** 0.5) + 1)]

cubes = [x ** 3 for x in xrange(1, int(limit ** (1.0/3)) + 1)]

palindomes = Counter()

for sq in sqs:
    for cube in cubes:
        n = sq + cube
        if palindromic(n):
            palindomes[n] += 1

print sum(x for x,_ in palindomes.most_common(5))
