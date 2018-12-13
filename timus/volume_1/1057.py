from functools import lru_cache

@lru_cache(maxsize=None)
def count_weights(n, k):
    """
    Return number of weight-k integers in [0, n] (for n >= 0, k >= 0)
    """
    if k == 0:
        return 1  # 0 is the only weight-0 value
    elif n == 0:
        return 0  # only considering 0, which doesn't have positive weight
    else:
        from_even = count_weights(n//b, k)
        from_odd = count_weights((n-1)//b, k-1)
        return from_even + from_odd

def count(x, k):
    while x:
        if x % b == 1: k -= 1
        x //= b
    return k == 0

x, y = [int(x) for x in input().split()]

k = int(input())
b = int(input())

print(count_weights(y, k) - count_weights(x, k) + count(x, k))
