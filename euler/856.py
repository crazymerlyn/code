from functools import cache

@cache
def func(c1, c2, c3, c4, last):
    res = 0
    total = c1 + c2*2 + c3*3 + c4*4
    if c1: res += (1+func(c1-1, c2, c3, c4, 1) * (c1-1 if last == 2 else c1)/c1) * c1/total
    if c2: res += (1+func(c1+1, c2-1, c3, c4, 2) * (c2-1 if last == 3 else c2)/c2) * 2*c2/total
    if c3: res += (1+func(c1, c2+1, c3-1, c4, 3) * (c3-1 if last == 4 else c3)/c3) * 3*c3/total

    # for cards with 4 copies left, no point in matching last
    if c4: res += (1+func(c1, c2, c3+1, c4-1, 4)) * 4*c4/total

    return res

print(round(func(0,0,0,13,-1), 8))
