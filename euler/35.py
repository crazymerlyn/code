def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def rotations(n):
    s = str(n)
    return [int(s[i:] + s[:i]) for i in range(len(s))]

count = 0
for n in range(2, 1000000):
    if all(is_prime(r) for r in rotations(n)):
        count += 1
print(count)
