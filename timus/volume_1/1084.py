from math import acos, pi
s, r = [int(x) for x in input().split()]

if r <= s / 2:
    print(pi * r * r)
elif r >= s / 2 ** 0.5:
    print(s * s)
else:
    theta = acos(s / 2 / r)
    cut = (r * r - s * s / 4) ** 0.5
    print("%.3f" % (2 * cut * s + (pi - theta * 4) * r * r))
