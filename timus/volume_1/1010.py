ys = [0]
for _ in range(int(input())):
    ys.append(int(input()))

a = max(range(2, len(ys)), key=lambda i: abs(ys[i] - ys[i-1]))

print(a-1, a)
