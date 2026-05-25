limit = 2000000
is_prime = [True] * (limit + 1)
total = 0
for i in range(2, limit):
    if is_prime[i]:
        total += i
        step = i
        start = i * i
        if start < limit:
            is_prime[start:limit:step] = [False] * ((limit - 1 - start) // step + 1)
print(total)
