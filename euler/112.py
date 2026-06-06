def is_bouncy(n):
    s = str(n)
    inc = all(s[i] <= s[i+1] for i in range(len(s)-1))
    dec = all(s[i] >= s[i+1] for i in range(len(s)-1))
    return not inc and not dec

count = 0
n = 1
while True:
    if is_bouncy(n):
        count += 1
    if count * 100 == 99 * n:
        print(n)
        break
    n += 1
