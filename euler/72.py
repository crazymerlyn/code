from utils import phi

limit = 10**6
res = 0
for n in range(2, limit+1):
    res += phi(n)
print(res)
