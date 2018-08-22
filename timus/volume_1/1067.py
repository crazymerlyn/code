def print_dir(d, offset=0):
    for k in sorted(d):
        print(" " * offset + k)
        print_dir(d[k], offset+1)

n = int(input())

d = {}

for _ in range(n):
    k = d
    for part in input().split('\\'):
        if part not in k:
            k[part] = {}
        k = k[part]

print_dir(d)
