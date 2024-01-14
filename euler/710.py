from functools import cache


n = 2000000

pal = [0] * (n+1)
oddpal = 0
evenpal = 0
pal2 = [0] * (n+1)
oddpal2 = 0
evenpal2 = 0

pal[0] = 1
evenpal = 1

for i in range(1, n+1):
    pal[i] = (1 + (oddpal if i % 2 else evenpal)) % 10**6
    oddpal += pal[i] if i % 2 else 0
    evenpal += pal[i] if i % 2 == 0 else 0

pal2[2] = 1
pal2[3] = 0

evenpal2 = 1

for i in range(4, n+1):
    pal2[i] = (pal[i-4] - pal2[i-4] + (oddpal2 if i % 2 else evenpal2)) % 10**6
    if pal2[i] == 0:
        print(i)
        break
    oddpal2 += pal2[i] if i % 2 else 0
    evenpal2 += pal2[i] if i % 2 == 0 else 0


