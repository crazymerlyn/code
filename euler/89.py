from utils import decimal_to_roman, roman_to_decimal

res = 0

with open("./p089_roman.txt") as f:
    for line in f:
        orig = line.strip()
        n = roman_to_decimal(orig)
        best = decimal_to_roman(n)
        assert len(best) <= len(orig)
        res += len(orig) - len(best)

print(res)

