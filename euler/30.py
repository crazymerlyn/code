def digit_power_sum(n, p):
    total = 0
    while n:
        total += (n % 10) ** p
        n //= 10
    return total

total = 0
for n in range(10, 1000000):
    if n == digit_power_sum(n, 5):
        total += n
print(total)
