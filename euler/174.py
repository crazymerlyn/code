from utils import factorize, product

limit = 10**6

count = 0
for n in range(8, limit+1, 4):
    k = n // 4
    l = product(p + 1 for _, p in factorize(k)) // 2

    if l <= 10:
        count += 1

print count

