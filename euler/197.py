def f(x):
    return int(2 ** (30.403243784 - x * x)) * 1e-9


x = -1

for _ in range(int(10000)):
    x = f(x)

print x + f(x)

