def solve(triangle):
    for r in range(len(triangle) - 2, -1, -1):
        for c in range(len(triangle[r])):
            triangle[r][c] += max(triangle[r+1][c], triangle[r+1][c+1])
    return triangle[0][0]

with open('p067_triangle.txt') as f:
    triangle = [list(map(int, line.strip().split())) for line in f]
print(solve(triangle))
