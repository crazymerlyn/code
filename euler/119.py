res = set()

for s in range(2, 1000):
    for p in range(2, 40):
        if sum(int(d) for d in str(s ** p)) == s:
            res.add(s ** p)

print sorted(res)[29]
