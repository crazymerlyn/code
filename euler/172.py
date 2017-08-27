from utils import comb

digits = 18
repeat = 3

def count(digits_left, choices):
    if choices > 1:
        return sum(comb(digits_left, c) * count(digits_left-c, choices-1) for c in range(min(digits_left+1, repeat+1)))
    return digits_left <= repeat

print count(digits, 10) * 9 / 10

