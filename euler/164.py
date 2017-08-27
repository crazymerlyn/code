from collections import defaultdict

limit = 19

def f(x, y, c):
    for i in range(10 - x - y):
        yield y, i, c

digs = {(0, i):1 for i in range(1, 10)}

for i in range(limit):
    newdigs = defaultdict(int)
    for ((x, y), c) in digs.items():
        for k, l, m in f(x, y, c):
            newdigs[(k, l)] += m
    digs = newdigs

print sum(digs.values())

