n = int(input())

a1 = int(round(float(input()) * 100))
a2 = int(round(float(input()) * 100))

s = 0
for i in range(n):
    ci = int(round(float(input()) * 100))
    s = s + (n - i) * ci

print("%.2f" % ((a1 + (a2 - a1 - s * 2) / (n + 1)) / 100))
