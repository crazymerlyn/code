from utils import fib

a = 0
b = 1
i = 0

limit = 10**9
digits = set("123456789")

while True:
    i += 1
    a, b = b, a + b
    a %= limit
    b %= limit
    if set(str(a)) == digits:
        if set(str(fib(i))[:9]) == digits:
            print i
            break

