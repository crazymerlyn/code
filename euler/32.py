from itertools import permutations

total = 0
seen = set()
for p in permutations('123456789'):
    s = ''.join(p)
    for i in range(1, 8):
        for j in range(i + 1, 9):
            a = int(s[:i])
            b = int(s[i:j])
            c = int(s[j:])
            if a * b == c:
                if c not in seen:
                    total += c
                    seen.add(c)
print(total)
