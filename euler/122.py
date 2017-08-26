minimum = {}
limit = 200

def calculate(path):
    m = max(path)
    if m > limit: return
    if m not in minimum: minimum[m] = path
    if len(path) > len(minimum[m]): return
    minimum[m] = path

    for p in path[::-1]:
        x = m + p
        calculate(path + [x])

calculate([1])
print sum(len(path) - 1 for path in minimum.values())

