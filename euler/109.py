def calculate_score(dart):
    a, b = dart[0], int(dart[1:])
    multiplier = ['', 'S', 'D', 'T']
    return b * multiplier.index(a)

possibs = []

for i in range(1, 21):
    possibs.extend(['S%d' % i, 'D%d' % i, 'T%d' % i])

possibs.append('S25')
possibs.append('D25')
possibs.append('S0')

ans = set()
for a in possibs:
    for b in possibs:
        for c in possibs:
            score = sum(map(calculate_score, [a, b, c]))
            if c[0] == 'D' and score < 100:
                ans.add((tuple(sorted([a, b, c])), c))
print len(ans)
