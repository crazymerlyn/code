count = [0, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
		'nine', 'ten', 'eleven', 'twelve','thirteen', 'fourteen', 'fifteen',
		'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty' ]

for _ in range(21, 1001):
	count.append('')

count[30] = 'thirty'
count[40] = 'forty'
count[50] = 'fifty'
count[60] = 'sixty'
count[70] = 'seventy'
count[80] = 'eighty'
count[90] = 'ninety'

for i in range(21, 1000):
	if i < 100:
		if i % 10 != 0:
			count[i] = count[i - i % 10] + count[i%10]
		else:
			continue
	else:
		count[i] = count[i/100] + 'hundred'
		
		if i % 100 != 0:
			count[i] += 'and' + count[i % 100]
		

count[-1] = 'onethousand'

print count

