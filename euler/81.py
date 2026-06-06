with open('p081_matrix.txt') as f:
    m = [[int(x) for x in line.split(',')] for line in f]
n = len(m)
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        top = m[i-1][j] if i > 0 else float('inf')
        left = m[i][j-1] if j > 0 else float('inf')
        m[i][j] += min(top, left)
print(m[n-1][n-1])
