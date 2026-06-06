total = 0
for a in range(3, 1001):
    # max remainder for (a-1)^n + (a+1)^n mod a^2
    total += 2 * a * ((a - 1) // 2)
print(total)
