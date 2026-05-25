import os
path = os.path.join(os.path.dirname(__file__), "p022_names.txt")
with open(path) as f:
    names = sorted(f.read().replace('"', '').split(','))

total = 0
for i, name in enumerate(names):
    score = sum(ord(c) - 64 for c in name) * (i + 1)
    total += score
print(total)
