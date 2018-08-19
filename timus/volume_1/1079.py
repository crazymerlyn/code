a = [0, 1]
for i in range(2, 10**5):
    if i % 2 == 0: a.append(a[i // 2])
    else:
        a.append(a[i // 2] + a[i // 2 + 1])

for i in range(1, 10**5):
    a[i] = max(a[i], a[i-1])
try:
    while True:
        n = int(input())
        if n == 0: break
        print(a[n])
except:
    pass
