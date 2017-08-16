m = 50
ways = [1]*m

limit = 10 ** 6
cur = 1


while cur <= limit:
    cur = ways[-1] + sum(ways[:-m]) + 1
    ways.append(cur)

print len(ways)-1

