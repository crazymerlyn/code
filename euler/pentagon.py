def pentagons(n):
    for i in xrange(1, n+1):
        yield i * (3*i - 1) / 2

ps = list(pentagons(10000))
p_set = set(ps)
m = float('inf')

for i in range(len(ps)):
    for j in range(i+1, len(ps)):
        if ps[j] - ps[i] in p_set and ps[j] + ps[i] in p_set:
            m = min(m, ps[j] - ps[i])

print m
