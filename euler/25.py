f1, f2 = 1, 1
idx = 2
while True:
    f1, f2 = f2, f1 + f2
    idx += 1
    if len(str(f2)) >= 1000:
        print(idx)
        break
