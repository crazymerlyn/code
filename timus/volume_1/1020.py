from math import pi

def dist(x, y):
    return sum((b - a) ** 2 for a, b in zip(x, y)) ** 0.5

n, r = [float(x) for x in input().split()]

ps = []
for _ in range(int(n)):
    ps.append([float(x) for x in input().split()])

ps += ps[:1]

res = pi * r * 2
for x, y in zip(ps, ps[1:]):
    res += dist(x, y)
print("%.2f" % res)
