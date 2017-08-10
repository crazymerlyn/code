from itertools import product, combinations

limit = 50
count = 0
for points in combinations(product(range(limit+1), repeat=2), 2):
    (x1, y1), (x2, y2) = points
    a = x1 ** 2 + y1 ** 2
    b = x2 ** 2 + y2 ** 2
    c = (x1 - x2) ** 2 + (y1 - y2) ** 2
    a, b, c = sorted([a, b, c])
    if c**0.5 < a**0.5 + b**0.5 and c == a + b:
        count += 1

print count
