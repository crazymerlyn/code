from utils import is_square

def continued_fraction(n):
    if is_square(n): return [int(n**0.5)]

    num = 0
    denom = 1
    rep = []
    while True:
        m = int((n**0.5 + num) / denom)
        rep.append(m)
        if m == 2 * int(n**0.5):
            return rep
        num, denom = denom * m - num, (n - (num - denom*m)**2) / denom

print sum(1 for i in range(1, 10001) if len(continued_fraction(i)) % 2 == 0)
