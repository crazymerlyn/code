from random import choice
from collections import defaultdict

w = 30
def possibs(i):
    if i >= w: yield i - w
    if i + w < 900: yield i + w
    if i % w: yield i - 1
    if i % w != w - 1: yield i + 1

ans = [1. for _ in range(900)]
for index in range(900):
    state = {index: 1.}
    for _ in range(50):
        newstate = defaultdict(float)
        for i in state:
            l = list(possibs(i))
            for j in l:
                newstate[j] += state[i] / len(l)
        state = newstate
    for i, val in state.items():
        ans[i] *= (1 - val)
print(sum(ans))

