n = 1000
s = [0 for _ in range(500500)]
t = 0
for k in range(500500):
    t = (615949 * t + 797807) & 0xfffff # Take modulo 2 ** 20
    s[k] = t - 2 ** 19

tri = [[0] for _ in range(n+1)]
sums = [[0] for _ in range(n+1)]

for row in range(1, n+1):
    for col in range(row):
        i = row * (row - 1) / 2 + col
        tri[row].append(s[i])

        sums[row].append(s[i] + sums[row][-1])

total_sums = [ar[:] for ar in tri]
result = 0
for row in range(1, n+1):
    for col in range(1, row+1):
        result = min(result, total_sums[row][col])

for size in range(2, n + 1):
    for start_row in range(1, n - size + 2):
        final_row = start_row + size - 1
        for i in range(1, start_row + 1):
            total_sums[start_row][i] += sums[final_row][i + size - 1] - sums[final_row][i-1]
            if total_sums[start_row][i] < result:
                result = total_sums[start_row][i]

print result

