n = 10 ** 6
m = 10 ** 9 + 7
res = 0
for k in range(2, n+1):
    res += ((pow(1 - k*k, n+1, m) - 1) * pow(-k*k, m-2, m) - 1) % m
    res %= m

print res

