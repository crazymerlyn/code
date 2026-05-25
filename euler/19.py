def is_leap(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dow = 1
count = 0
for y in range(1900, 2001):
    for m in range(12):
        if y > 1900 and dow == 0:
            count += 1
        dow = (dow + days[m] + (1 if m == 1 and is_leap(y) else 0)) % 7
print(count)
