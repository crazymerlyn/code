a = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
b = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"

sizes = [len(a), len(b)]
while sizes[-1] < (127 + 19 * 17) * 7 ** 17:
    sizes.append(sizes[-1] + sizes[-2])

def f(i, chs):
    if i == 0: return int(a[chs-1])
    if i == 1: return int(b[chs-1])

    if chs <= sizes[i-2]:
        return f(i-2, chs)
    else:
        return f(i-1, chs - sizes[i-2])

def dab(n):
    if n <= len(a):
        return int(a[n-1])
    i = 0
    while sizes[i] < n:
        i += 1
    return f(i-1, n - sizes[i-2])

res = 0
for n in range(18):
    i = (127 + 19 * n) * 7 ** n
    res += 10 ** n * dab(i)
print(res)
