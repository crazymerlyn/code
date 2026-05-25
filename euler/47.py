def factor_count(n):
    cnt = 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            cnt += 1
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        cnt += 1
    return cnt

n = 1
while True:
    if all(factor_count(n + i) == 4 for i in range(4)):
        print(n)
        break
    n += 1
