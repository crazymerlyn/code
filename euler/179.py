limit = 10 ** 7

ndiv = [1 for _ in range(limit+1)]

for i in xrange(2, limit+1):
    for j in xrange(i, limit+1, i):
        ndiv[j] += 1

count = 0
for i in xrange(2, limit):
    if ndiv[i] == ndiv[i+1]:
        count += 1
print count

