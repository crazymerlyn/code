def guest_no(f, r):
    if f == 1: return r * (r + 1) // 2
    start = f * f // 2
    if f % 2 == 0:
        if r % 2 == 0:
            return start + (4 * f + 2 + 4 * (r // 2 - 1)) * r // 4
        else:
            return start + (4 * f + 6 + 4 * (r // 2 - 1)) * (r // 2) // 2
    else:
        if r % 2 == 0:
            return start + 1 + (4 * f + 6 + 4 * (r // 2 - 2)) * (r-2) // 4
        else:
            return start + (4 * f + 2 + 4 * (r // 2 - 1)) * (r // 2) // 2

res = 0
n = 2 ** 27 * 3 ** 12
for i in range(28):
    for j in range(13):
        f = 2 ** i * 3 ** j
        res += guest_no(f, n // f)
print(res % 10 ** 8)
