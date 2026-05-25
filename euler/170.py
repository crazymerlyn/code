from itertools import permutations

PAND = (1 << 10) - 1
best = 0

def digits_mask(x):
    m = 0
    while x:
        m |= 1 << (x % 10)
        x //= 10
    return m

for p in permutations('0123456789'):
    s = ''.join(p)
    for n_len in range(1, 9):
        n_end = n_len
        if s[0] == '0':
            break
        n = int(s[:n_len])
        for a_len in range(1, 10 - n_len):
            a_end = n_len + a_len
            if s[n_len] == '0':
                continue
            b_len = 10 - n_len - a_len
            if b_len < 1:
                continue
            if s[a_end] == '0':
                continue
            a = int(s[n_len:a_end])
            b = int(s[a_end:])
            p1 = n * a
            p2 = n * b
            m = digits_mask(p1) | digits_mask(p2)
            if m == PAND:
                val = int(str(p1) + str(p2))
                if val > best:
                    best = val

print(best)
