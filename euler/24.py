from math import factorial

digits = list(range(10))
n = 1000000 - 1
result = []
for i in range(9, -1, -1):
    f = factorial(i)
    idx = n // f
    n %= f
    result.append(str(digits.pop(idx)))
print(''.join(result))
