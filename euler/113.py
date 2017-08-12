def comb(n, r):
    num = 1
    denom = 1
    for i in range(1, r+1):
        num *= n - i + 1
        denom *= i
    return num // denom

digits = 100

print comb(digits + 9, 9) + comb(digits + 10, 10) - 10 * digits - 2

