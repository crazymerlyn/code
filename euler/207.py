from math import log

i = 0
j = 0
for x in range(2, 1000000):
    k = x * (x - 1)
    i += 1
    if log(x, 2) % 1 == 0:
        j += 1

    if j * 12345 < i:
        print k
        break

