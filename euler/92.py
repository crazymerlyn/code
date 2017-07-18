end = [0 for _ in range(10000001)]

end[1] = 1
end[89] = 89

def sq_dig_sum(n):
    return sum(int(d)**2 for d in str(n))

for i in range(2, 10000001):
    n = sq_dig_sum(i)
    to_update = [i]
    while not end[n]:
        to_update.append(n)
        n = sq_dig_sum(n)

    for j in to_update:
        end[j] = end[n]

print sum(x == 89 for x in end)

