index = 124
i = 0
n = 1

while i < index:
    t1, t2, t3 = 1, 1, 3
    while t3 % n != 0 and (t1, t2, t3) != (1, 1, 1):
        t1, t2, t3 = t2, t3, (t1 + t2 + t3) % n
    if t3 % n != 0:
        i += 1
    n += 2

print n - 2

