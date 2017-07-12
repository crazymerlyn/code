def digits(n):
	result = []
	while n > 0:
		result.append(n % 10)
		n /= 10
	
	return result

fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def sum_to(n):
	result = 0
	for i in range(3, n+1):
		if sum([fact[x] for x in digits(i)]) == i:
			result += i
	
	return result
