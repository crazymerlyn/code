limit = 10 ** 12
n = (limit + 3) // 4
ans = 0
for i in range(64):
    if n & (1 << i):
        ans = ans * 2 + 3 ** i
print(ans)
