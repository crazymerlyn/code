from math import factorial

facts = [factorial(i) for i in range(10)]

total = 0
for n in range(10, 100000):
    s = 0
    m = n
    while m:
        s += facts[m % 10]
        m //= 10
    if s == n:
        total += n
print(total)
