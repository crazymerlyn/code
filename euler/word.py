import math
import time

def number(word):
	return sum([ord(ch) - ord('a') + 1 for ch in word])


result = 0

start = time.time()

words = raw_input().strip().split(',')
words = [word[1:-1].lower() for word in words]

for word in words:
	count = number(word)
		
	c = 2 * count
		
	d = math.sqrt(1 + 4*c)
		
	if d == math.floor(d) and d % 2 == 1:
		result += 1
print result
print 'time taken = ', time.time() - start
