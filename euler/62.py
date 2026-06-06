from collections import defaultdict

cubes = defaultdict(list)
n = 1
while True:
    cube = n ** 3
    key = ''.join(sorted(str(cube)))
    cubes[key].append(cube)
    if len(cubes[key]) == 5:
        print(cubes[key][0])
        break
    n += 1
