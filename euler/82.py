with open('p082_matrix.txt') as f:
    m = [[int(x) for x in line.split(',')] for line in f]
n = len(m)
dp = [row[0] for row in m]
for col in range(1, n):
    col_vals = [m[i][col] for i in range(n)]
    new = [dp[i] + col_vals[i] for i in range(n)]
    for i in range(1, n):
        new[i] = min(new[i], new[i-1] + col_vals[i])
    for i in range(n-2, -1, -1):
        new[i] = min(new[i], new[i+1] + col_vals[i])
    dp = new
print(min(dp))
