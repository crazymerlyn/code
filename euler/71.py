LIMIT = 1000000
a, b = 0, 1
for q in range(2, LIMIT + 1):
    p = (3 * q - 1) // 7
    if a * q < b * p:
        a, b = p, q
print(a)
