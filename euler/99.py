with open('base_exp.txt') as f:
    res = None
    m = 0
    from math import log
    for i, line in enumerate(f):
        a, b = map(int, line.strip().split(","))
        if m < log(a) * b:
            m = log(a) * b
            res = i
    print res + 1
