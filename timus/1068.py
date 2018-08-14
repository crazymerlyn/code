n = int(input())

if n >= 1:
    print(n * (n+1)//2)
elif n == 0:
    print(1)
else:
    n = -n
    print(1 - n * (n+1)//2)
