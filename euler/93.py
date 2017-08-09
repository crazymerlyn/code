from itertools import permutations, combinations, product

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return 1.0*a / b if b else 0

max_n = 0
choice = None
for digits in combinations(range(1, 10), 4):
    possibs = set()
    for perm in permutations(digits, 4):
        perm = list(perm)
        for op_order in product([add, sub, mul, div], repeat=3):
            for order in product([0, 1, 2], [0, 1], [0]):
                op_order1 = list(op_order)
                res = list(perm)
                for index in order:
                    op = op_order1.pop(index)
                    a = res.pop(index)
                    b = res.pop(index)
                    res.insert(index, op(a, b))
                possibs.add(res[0])

    for i in range(1, len(possibs)):
        if i not in possibs:
            break
    if i - 1 > max_n:
        max_n = i - 1
        choice = digits
print choice

