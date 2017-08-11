a0, b0, a1, b1 = 1, -1, 1, 1

limit = 2 * 10 ** 12 - 1

while b0 <= limit:
    a0, a1 = a1, 6*a1 - a0
    b0, b1 = b1, 6*b1 - b0

print (a0 + 1) // 2


