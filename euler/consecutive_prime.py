def n_dist_fact(n):
	result = 0
	
	if n % 2 == 0:
		while n % 2 == 0:
			n = n / 2
		result += 1
	
	i = 3
	while i <= n:
		if n % i == 0:
			result += 1
			while n % i == 0:
				n = int(n/i)
		i += 2
	
	return result

prime = [1, 2, 3, 8, 25, 11]

def consecutive(n):
	i = prime[n] ** n
	count = 0
	while True:
		i += 1
		if n_dist_fact(i) == n:
			count += 1
		else:
			count = 0
		
		if count == n:
			return range(i-n+1, i+1)
