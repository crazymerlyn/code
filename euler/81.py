with open('p081_matrix.txt') as f:
    grid = [list(map(int, line.strip().split(','))) for line in f]

n = len(grid)
for i in range(1, n):
    grid[i][0] += grid[i-1][0]
    grid[0][i] += grid[0][i-1]
for i in range(1, n):
    for j in range(1, n):
        grid[i][j] += min(grid[i-1][j], grid[i][j-1])
print(grid[n-1][n-1])
