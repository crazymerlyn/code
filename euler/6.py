def solve():
    n = 100
    sum_sq = n * (n + 1) * (2 * n + 1) // 6
    sq_sum = (n * (n + 1) // 2) ** 2
    print(sq_sum - sum_sq)

solve()
