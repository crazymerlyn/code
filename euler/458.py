from utils import mat_mul

m = []
for i in range(1, 7):
    m.append([1] * i + [7 - i] + [0] * (7 - i - 1))
m.append([0] * 6 + [7])

n = 10 ** 12
mod = 10 ** 9

res = [[0 for _ in range(7)] for _ in range(7)]
for i in range(7): res[i][i] = 1
while n:
    if n % 2:
        res = mat_mul(res, m, mod)
    m = mat_mul(m, m, mod)
    n //= 2

print(7 * res[0][0] % mod)
