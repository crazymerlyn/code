from utils import is_square

def solve_eq_for(d):
    """ Solve for minimum integer x: x**2 - d*y**2 = 1 """
    x0, y0 = 0, 1
    x1, y1 = 1, 0
    n = d
    num = 0
    denom = 1
    while True:
        m = int((n**0.5 + num) / denom)
        x, y = m*x1 + x0, m*y1 + y0
        x0, y0 = x1, y1
        x1, y1 = x, y
        num, denom = denom * m - num, (n - (num - denom*m)**2) / denom

        if x*x - d*y*y == 1:
            return x

    return -1

res = None
max_x = 0

for d in range(1, 1001):
    if is_square(d): continue
    x = solve_eq_for(d)
    if x > max_x:
        max_x = x
        res = d
print(res)

