idxs = []

for i in range(4):
    line = input()
    idxs.extend([(i, j) for j, x in enumerate(line) if x == 'X'])

mat = []
for _ in range(4):
    mat.append(input())

res = ""
for _ in range(4):
    for i, j in idxs: res += mat[i][j]
    idxs = sorted((j, 3 - i) for i, j in idxs)
print(res)
