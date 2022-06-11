mod = 10**9 + 7

def s(n):
    n, r = n // 9, n % 9

    res = pow(10, n, mod) * 6 - 9*n - 6
    res += r * (r+3)//2 * pow(10, n, mod) - r

    return res % mod

fib = [0, 1]
for _ in range(90): fib.append(fib[-2] + fib[-1])

print(sum(s(fib[i]) for i in range(2, 91)) % mod)
