limit = 10 ** 9

def s(n):
    res = 1

    if n < 7: return n * (n + 1) / 2

    p = 1
    while p * 7 <= n:
        p *= 7
        res *= 28

    m = n // p
    ans = res
    for i in range(2, m+1):
        ans += i * res

    ans += s(n % p) * (m + 1)

    return ans

print s(10**9)
