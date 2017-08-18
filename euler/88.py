def prodsum(p, s, c, start):
    k = p - s + c
    if k < kmax:
        if p < n[k]: n[k] = p
        for i in xrange(start, kmax//p*2 + 1):
            prodsum(p*i, s+i, c+1, i)

kmax = 12001
n = [2*kmax] * kmax

prodsum(1, 1, 1, 2)

print sum(set(n[2:]))
