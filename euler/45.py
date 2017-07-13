def is_pentagonal(n):
    i = (1 + (1 + 24*n) ** 0.5) / 6
    return i % 1 == 0

def is_hexagonal(n):
    i = (1 + (1 + 8*n) ** 0.5) / 4
    return i % 1 == 0

for i in range(1, 100000):
    n = i * (i + 1) / 2
    if is_pentagonal(n) and is_hexagonal(n):
        print i, n

