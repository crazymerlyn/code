from random import randint, seed
from collections import Counter

CH = [0, 10, 11, 24, 39, 5]
CC = [0, 10]

def next_rail(pos):
    if pos < 5 or pos >= 35:
        return 5
    if pos < 15:
        return 15
    if pos < 25:
        return 25
    return 35

def next_util(pos):
    if pos < 12 or pos >= 28:
        return 12
    return 28

def process_cc(pos):
    card = randint(0, 15)
    if card < 2:
        return CC[card]
    return pos

def process_ch(pos):
    card = randint(0, 15)
    if card < 6:
        return CH[card]
    if card == 6 or card == 7:
        return next_rail(pos)
    if card == 8:
        return next_util(pos)
    if card == 9:
        pos = (pos - 3) % 40
        if pos in (2, 17, 33):
            return process_cc(pos)
        return pos
    return pos

seed(0)
pos = 0
doubles = 0
counts = Counter()
trials = 5000000
for _ in range(trials):
    d1, d2 = randint(1, 4), randint(1, 4)
    if d1 == d2:
        doubles += 1
    else:
        doubles = 0
    if doubles == 3:
        pos = 10
        doubles = 0
    else:
        pos = (pos + d1 + d2) % 40
        if pos == 30:
            pos = 10
        elif pos in (7, 22, 36):
            pos = process_ch(pos)
        elif pos in (2, 17, 33):
            pos = process_cc(pos)
    counts[pos] += 1

result = ''.join(f'{k:02d}' for k, _ in counts.most_common(3))
print(result)
