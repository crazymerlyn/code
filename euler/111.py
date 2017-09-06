from utils import is_prime2 as isprime

digits = 10

number = [0] * digits

def check_number():
    if not number[0]: return 0
    n = int("".join(map(str, number)))
    return n if isprime(n) else 0

def count(digit, pos, left):
    if not left: return check_number()
    res = 0
    for i in range(pos, len(number)):
        for val in range(0, 10):
            number[i] = val
            res += count(digit, pos+1, left-1)
            number[i] = digit
    return res

result = 0
for digit in range(0, 10):
    for left in range(1, len(number)):
        for i in range(len(number)): number[i] = digit
        s = count(digit, 0, left)
        if s:
            result += s
            break

print result

