def is_triangle(t):
    n = int((2 * t) ** 0.5)
    return n * (n + 1) // 2 == t

with open("p042_words.txt") as f:
    words = f.read().replace('"', '').split(',')

count = 0
for w in words:
    s = sum(ord(c) - ord('A') + 1 for c in w)
    if is_triangle(s):
        count += 1
print(count)
