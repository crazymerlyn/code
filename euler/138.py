from utils import is_square

p, q, k, r, s, l = -9, -4, 4, -20, -9, 8

sols = [(8, 17)]
n = 12

for _ in range(n-1):
    x, y = sols[-1]
    sols.append((p * x + q * y + k, r * x + s * y + l))

sols = [int(abs(y)) for _,y in sols]

print sum(sols)

