import sys
for line in sys.stdin:
    a = [line[i:i+32] for i in range(0,len(line),32)]
    if len(a) > len(set(a)):
        print(a)
