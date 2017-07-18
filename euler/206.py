ends = [3, 7]
newends = []


ends = [3, 7]
newends = []
for i in range(8):
    for base in range(0, 100):
        for end in ends:
            n = base * (10 ** (2*i + 1)) + end
            if n > 10**11: break
            sq = n ** 2
            if (sq % (10 ** (2*i + 3))) / (10 ** (2* i + 2)) == 8-i:
                newends.append(n)
    ends = newends
    print len(ends)
    newends = []

print ends[0], ends[0] ** 2
