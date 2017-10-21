import random
from utils import memoized

@memoized
def ans(*batch):
    if batch == (1,):
        return 1

    count = 0
    if len(batch) == 1:
        count = 1

    res = 0.0
    for i in range(len(batch)):
        res += count + ans(*sorted(batch[:i] + batch[i+1:] + tuple(range(1, batch[i]))))
    res /= len(batch)
    return res

print ans(5) - 2
