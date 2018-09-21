from utils import comb
from math import factorial
from decimal import Decimal

def possibs(same, total):
    res = 0
    for ncorrect in range(1, same+1):
        res += comb(same, ncorrect) * factorial(total - ncorrect) * (1 if ncorrect % 2 else -1)
    return res

print(Decimal(comb(25, 3) * (factorial(97) - possibs(22, 97))) / factorial(100))
