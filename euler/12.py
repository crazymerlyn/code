def count_divisors(n):
    cnt = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            cnt += 1
            if i * i != n:
                cnt += 1
        i += 1
    return cnt

i = 1
while True:
    t = i * (i + 1) // 2
    if count_divisors(t) > 500:
        print(t)
        break
    i += 1
