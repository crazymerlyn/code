from utils import is_square

def combs(x, y, z):
    return (x+y, x-y, x+z, x-z, y+z, y-z)

l = 1000
for i in range(1, l):
    e = i * i
    for j in range(i+1, l):
        c = j * j
        if not is_square(c-e): continue
        off = 2 - i % 2
        for k in range(j+off, int((c + e) ** 0.5) + 1, 2):
            a = k * k
            if all(is_square(x) for x in (a-c, a-e, c-e)):
                print (a + c + e) / 2

