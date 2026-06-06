from math import comb
# non-decreasing: choose 9 positions out of (100 + 9 - 1) = choose(108, 9)
# non-increasing: choose 10 positions out of (100 + 10 - 1) = choose(109, 10) - 1 - 100*9
# (subtract 1 for all-zero, subtract 100*9 for numbers starting with 0)
n = comb(100 + 9, 9) + comb(100 + 10, 10) - 1 - 100 * 9
print(n)
