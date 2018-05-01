from math import factorial
from itertools import groupby

fac = [factorial(i) for i in range(21)]
choices = [12 for _ in range(20)]

def calc():
    res = fac[20]
    for _, g in groupby(choices):
        res //= fac[len(list(g))]
    return res

res = 0
target = 70
def func(i):
    global res
    if i == 20:
        res += calc()
        return
    if i == 10 and sum(choices[:10]) != target:
        return
    c = 12 if not i else choices[i-1]
    for j in range(1, c+1):
        choices[i] = j
        func(i+1)
func(0)
print(res)
