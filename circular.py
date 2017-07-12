import math

is_prime = [True for _ in range(0, 1000001)]

for i in xrange(2, 1000000):
	if is_prime[i]:
		for j in range(i, (1000000 / i) + 1):
			is_prime[i * j] = False

def rotate(n):
	n_str = str(n)
	n_str = n_str[-1] + n_str[:-1]
	
	return int(n_str)


def is_circular_prime(n):
	if not is_prime[n]:
		return False

	orig = n
	n = rotate(n)
	
	while orig != n:
		if not is_prime[n]:
			return False
		
		n = rotate(n)
	
	return True
