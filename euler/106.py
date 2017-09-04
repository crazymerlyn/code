from utils import catalan, comb

n = 12
res = 0
for i in range(1, n/2+1):
    res += comb(n, i) * comb(n - i, i) / 2 - catalan(i) * comb(n, 2*i)

print res

