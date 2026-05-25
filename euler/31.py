coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [0] * 201
ways[0] = 1
for c in coins:
    for i in range(c, 201):
        ways[i] += ways[i - c]
print(ways[200])
