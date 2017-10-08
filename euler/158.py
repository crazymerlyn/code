from math import factorial

def comb(n, r):
    if r > n: return 0
    return factorial(n) / factorial(n - r) / factorial(r)

def p(n):
    base = comb(26, n)
    res = 0

    for right in range(2, n+1):
        for left in range(1, right):
            middle = right - left - 1
            greater = n - right
            for lcount in range(n-right, n - left):
                for middlecount in range(lcount-greater, min(lcount, middle) + 1):
                    if (left - 1 + middle - middlecount) < (n - lcount - 2): continue
                    count = comb(middle, middlecount) * comb(greater, lcount-middlecount)
                    res += count

    return base * res

print max(p(n) for n in range(1, 27))

