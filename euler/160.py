from utils import factors_in_factorial, memoized

limit = 10 ** 5

@memoized
def coprimefact(n):
    res = 1
    for i in range(1, n+1):
        if i % 2 == 0 or i % 5 == 0: continue
        res *= i
        res %= limit
    return res

def fact(n, allow_even=True):
    if n <= 1: return 1
    evens = fact(n//2) if allow_even else 1
    return evens * fact(n//5, False) * coprimefact(n % 10 ** 5) % 10 ** 5

def last5(n):
    extra_twos = factors_in_factorial(n, 2) - factors_in_factorial(n, 5)

    return fact(n) * pow(2, extra_twos, limit) % 10 ** 5

print(last5(10 ** 12))

