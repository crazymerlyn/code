from fractions import Fraction

s = 290797
t = []
for _ in range(20000):
    s = s * s % 50515093
    t.append(s % 500)

segs = [(t[i], t[i+1], t[i+2], t[i+3]) for i in range(0, 20000, 4)]

points = set()
for i in range(len(segs)):
    x0, y0, x1, y1 = segs[i]
    for j in range(i + 1, len(segs)):
        x2, y2, x3, y3 = segs[j]

        denom = (x0 - x1) * (y2 - y3) - (x2 - x3) * (y0 - y1)
        if denom == 0:
            continue

        numer0 = (x0 - x2) * (y2 - y3) - (x2 - x3) * (y0 - y2)
        numer1 = (x1 - x0) * (y0 - y2) - (x0 - x2) * (y1 - y0)

        t0 = Fraction(numer0, denom)
        t1 = Fraction(numer1, denom)
        if 0 < t0 < 1 and 0 < t1 < 1:
            points.add((x0 + t0 * (x1 - x0), y0 + t0 * (y1 - y0)))

print(len(points))
