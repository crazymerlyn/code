mod = 4503599627370517
n = 1504170715041707
res = 1
while n > 1:
    res += n
    n, mod = n - mod % n, n
print(res) 

