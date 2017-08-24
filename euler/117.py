ways = [0, 1, 2, 4, 8]

n = 50
for i in range(5, n+1):
    ways.append(ways[-1] + ways[-2] + ways[-3] + ways[-4])

print ways[n]
