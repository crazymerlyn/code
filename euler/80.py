from utils import is_square

from decimal import Decimal, getcontext

getcontext().prec=120

res = 0

for n in range(1, 101):
    if is_square(n): continue
    root = Decimal(n) ** Decimal(0.5)
    res += sum(int(d) for d in str(root).replace(".", "")[:100])
print(res)
