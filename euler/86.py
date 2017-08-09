from utils import is_square

limit = 10**6
cur = 0

m = 2

while cur <= limit:
    m += 1
    for ab in range(3, 2*m):
        if is_square(ab*ab + m*m):
            cur += min(ab, m+1) - (ab+1)//2

print m

