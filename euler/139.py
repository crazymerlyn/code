x = 1
y = 1
limit = 10 ** 8
res = 0

while x + y < limit:
    x, y = 3 * x + 4 * y, 2 * x + 3 * y
    print x, y, (x+1)/2, (x-1)/2, y, x + y

    p = x + y
    res += limit // p


print res
