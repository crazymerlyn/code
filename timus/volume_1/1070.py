def time(x):
    h, s = x.split('.')
    return int(h) * 60 + int(s)

a, b = [time(x) for x in input().split()]
c, d = [time(x) for x in input().split()]

diff1 = (b - a + 1440) % 1440
diff2 = (d - c + 1440) % 1440

airport_diff = abs(diff2 - diff1) / 2
if airport_diff * 2 >= 720: airport_diff = 720 - airport_diff


print(int(round(airport_diff / 60)))
