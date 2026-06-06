# Reversible numbers below 10^9
# Only even-length numbers work.
# DP going from outermost pair (units + most significant) to innermost pair.

# Inner pair: both digits 0-9
# For each carry_in 0/1, how many (a,b) produce odd sum and carry_out 0/1?
inner = [[0, 0], [0, 1]]  # placeholder
inner[0][0] = sum(1 for a in range(10) for b in range(10) if (a+b) % 2 == 1 and a+b < 10)
inner[0][1] = sum(1 for a in range(10) for b in range(10) if (a+b) % 2 == 1 and a+b >= 10)
inner[1][0] = sum(1 for a in range(10) for b in range(10) if (a+b+1) % 2 == 1 and a+b+1 < 10)
inner[1][1] = sum(1 for a in range(10) for b in range(10) if (a+b+1) % 2 == 1 and a+b+1 >= 10)

# Outer pair: leading digit 1-9, last digit 1-9, carry_in=0
outer0 = [0, 0]
outer0[0] = sum(1 for a in range(1, 10) for b in range(1, 10) if (a+b) % 2 == 1 and a+b < 10)
outer0[1] = sum(1 for a in range(1, 10) for b in range(1, 10) if (a+b) % 2 == 1 and a+b >= 10)

total = 0
for L in (2, 4, 6, 8):
    ways = [outer0[0], outer0[1]]  # carries after outermost level
    for _ in range(L // 2 - 1):
        ways = [ways[0]*inner[0][0] + ways[1]*inner[1][0],
                ways[0]*inner[0][1] + ways[1]*inner[1][1]]
    total += sum(ways)

print(total)
