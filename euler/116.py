limit = 50
res = 0

red = [0, 0, 1, 2]

for i in range(4, limit+1):
    a, b = red[-2], red[-3]
    red.append(2 * (1 + a) + b)
res += red[50]

green = [0, 0, 0, 1, 2]
for i in range(5, limit+1):
    a, b, c = green[-3], green[-4], green[-5]
    green.append(1 + a + 1 + b + 1 + c + a)
res += green[50]


blue = [0, 0, 0, 0, 1, 2, 3]
for i in range(6, limit+1):
    a, b, c, d = blue[-4], blue[-5], blue[-6], blue[-7]
    blue.append(1 + a + 1 + b + 1 + c + 1 + d + a)
res += blue[50]

print res


