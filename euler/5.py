def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = 1
for i in range(2, 21):
    n = n * i // gcd(n, i)
print(n)
