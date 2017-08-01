def sign(p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

def origin_in_triangle(p1, p2, p3):
    origin = (0, 0)
    b1 = sign(origin, p1, p2) < 0.0
    b2 = sign(origin, p2, p3) < 0.0
    b3 = sign(origin, p3, p1) < 0.0

    return b1 == b2 and b2 == b3

res = 0
with open("./p102_triangles.txt") as f:
    for line in f:
        x1, y1, x2, y2, x3, y3 = map(int, line.strip().split(','))
        p1 = (x1, y1)
        p2 = (x2, y2)
        p3 = (x3, y3)
        if origin_in_triangle(p1, p2, p3):
            res += 1

print(res)

