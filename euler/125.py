def is_palindrome(n):
    return str(n) == str(n)[::-1]

limit = 10**8
res = set()
for a in range(1, 10**4):
    for k in range(2, 1500):
        s = a * a * k + a * k * (k - 1) + k * (k - 1) * (2 * k - 1) // 6
        if s > limit: break
        if is_palindrome(s):
            res.add(s)

print sum(res)
