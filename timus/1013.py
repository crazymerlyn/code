def mat_mul(a, b, m):
    c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            c[i][j] = sum(a[i][k] * b[k][j] for k in range(2)) % m
    return c

def mat_pow(a, p, m):
    res = [[1, 0], [0, 1]]
    while p:
        if p % 2: res = mat_mul(res, a, m)
        a = mat_mul(a, a, m)
        p //= 2
    return res

def res(n):
    start = [[(k-1)**2,k-1],[k-1,0]]
    mat = [[k-1, k-1], [1, 0]]
    return mat_mul(start, mat_pow(mat, n-1, m), m)[1][0]

n = int(input())
k = int(input())
m = int(input())

print((res(n-1) + res(n)) % m)
