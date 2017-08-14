res = 0
for i in range(1000):
    res += 1 - (1 - 1.0/2**i)**32
print res

