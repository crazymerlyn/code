res = 0
for i in range(1, 10):
    if i % 2 == 0:
        res += 20 * 30 ** (i//2 - 1)
    elif i % 4 == 3:
        res +=  100 * 500 ** (i // 4)
print res
