def diagonals(a, b):
    if a < b: a, b = b, a
    return b * ((2 * a - b) * (4 * b * b - 1) - 3) // 6

h = 47
w = 43
res = 0
for a in range(1, h+1):
    for b in range(1, w+1):
        res += a * b * (a + 1) * (b + 1) // 4
        res += diagonals(a, b)
print(res)
