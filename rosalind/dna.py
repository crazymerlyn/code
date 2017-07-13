count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for c in raw_input():
    count[c] += 1


print count['A'], count['C'], count['G'], count['T']
