m = -19.7 / 1.4
x, y = (1.4, -9.6)

count = 0

while True:
    if -0.01 <= x <= 0.01 and y > 0: break
    count += 1

    normal_m = y / (4 * x)
    tan2m = 2 * normal_m / (1 - normal_m * normal_m)
    m = (tan2m - m) / (1 + tan2m * m)
    c = y - m * x

    # (m2 + 4)x2 + 2mcx + c2 - 100 = 0
    # x = (-mc +- sqrt(100m2 + 400 - 4c2)) / (m2 + 4)

    d = 100 * m * m - 4 * c * c + 400
    x1 = (- m * c + d ** 0.5) / (m * m + 4)
    x2 = (- m * c - d ** 0.5) / (m * m + 4)

    if abs(x1 - x) < 1e-3:
        x = x2
    else:
        x = x1

    y = m * x + c

print count
