limit = 60000

p = [0 for _ in range(limit+1)]
p[0] = 1
sigma = [0 for _ in range(limit+1)]
for n in range(1, limit+1):
    sigma[n] = sum(sum(set([x, n//x])) for x in range(1, int(n**0.5)+1) if n % x == 0)

for n in range(1, limit+1):
    p[n] = 0
    sign = 1
    k = 1
    while k * (3*k - 1) // 2 <= n:
        i = k * (3*k - 1) // 2
        if 1 <= i <= n:
            p[n] += sign * p[n-i]
        i = k * (3*k + 1) // 2
        if 1 <= i <= n:
            p[n] += sign * p[n-i]
        sign *= -1
        k += 1
    p[n] %= 10**6
    if p[n] % 10**6 == 0:
        print n
        break

