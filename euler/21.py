def d(n):
    s = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            s += i
            if i * i != n:
                s += n // i
        i += 1
    return s

total = 0
for a in range(2, 10000):
    b = d(a)
    if b > a and d(b) == a:
        total += a + b
print(total)
