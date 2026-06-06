LIMIT = 100
ways = [0] * (LIMIT + 1)
ways[0] = 1
for i in range(1, LIMIT):
    for j in range(i, LIMIT + 1):
        ways[j] += ways[j - i]
print(ways[LIMIT])
