from fractions import gcd

n, m = [int(x) for x in input().split()]

n -= 1
m -= 1

res = n + m

res -= gcd(n, m)
print(res)
