a = raw_input()
b = raw_input()
print sum(x != y for x,y in zip(a,b))
