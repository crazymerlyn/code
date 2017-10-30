def step(n):
    if n % 3 == 0:
        return (n/3, "D")
    if n % 3 == 1:
        return ((4 * n + 2) / 3, "U")
    return ((2 * n - 1) / 3, "d")

def get_seq(n):
    res = ""
    while n != 1:
        n, s = step(n)
        res += s
    return res

def get_n(n, s):
    for c in s[::-1]:
        if c == "D":
            n *= 3
        elif c == "d":
            if n * 3 % 2 == 0: return False
            n = ((n * 3) + 1) / 2
        else:
            if n * 3 % 4 != 2: return False
            n = ((n * 3) - 2) / 4
    return n

s = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
n = 96521732651065
fact = 3 ** len(s)

limit = 10 ** 15

print n + limit/fact * fact + fact

