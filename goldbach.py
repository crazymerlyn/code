import math

def check(n):
	is_prime = [True for _ in range(n)]
	
	is_prime[0] = is_prime[1] = False
	
	for i in range(2, int(math.sqrt(n))):
		if is_prime[i]:
			for j in range(i*i, n, i):
				is_prime[j] = False
	
	for i in range(5, n, 2):
		for j in range(int(math.sqrt(i//2)) + 1):
			#print i, j, i- 2 * j**2
			#print "is_prime:", is_prime[i], is_prime[i - 2*j**2]
			if is_prime[i - 2 * j**2]:
				break
		else:
			return i
