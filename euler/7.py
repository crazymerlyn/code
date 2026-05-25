def solve():
    limit = 200000
    is_prime = [True] * (limit + 1)
    count = 0
    for i in range(2, limit + 1):
        if is_prime[i]:
            count += 1
            if count == 10001:
                print(i)
                return
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

solve()
