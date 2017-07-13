from math import factorial
from itertools import permutations

n = int(raw_input())

print factorial(n)

for p in permutations(range(1, n+1)):
    print " ".join(map(str, p))

