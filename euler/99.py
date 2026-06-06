import math
with open('base_exp.txt') as f:
    pairs = [line.strip().split(',') for line in f]
max_line, max_val = 0, 0
for i, (b, e) in enumerate(pairs):
    val = int(e) * math.log(int(b))
    if val > max_val:
        max_val = val
        max_line = i + 1
print(max_line)
