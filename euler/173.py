from math import ceil

limit = 10**6

count = 0
for i in range(3, limit//4+4):
    m = int(ceil(max(1, i*i-limit)**0.5))
    count += (i-m)//2
print count

