import math

def sum_factors(num):
	return sum([x for x in range(1, num) if num % x == 0])


amicables = set()

for i in range(1, 10001):
	if i not in amicables:
		f_sum = sum_factors(i)
		if f_sum != i and i == sum_factors(f_sum):
			amicables.add(i)
			amicables.add(f_sum)

print sum(amicables)
