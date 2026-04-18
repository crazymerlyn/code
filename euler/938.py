def solve_p_bottom_up(R, B):
    """
    Calculates P(R, B) using iterative bottom-up DP.
    R: Number of red cards (must be even for P > 0)
    B: Number of black cards
    """
    if R % 2 != 0:
        return 0.0
    if R == 0:
        return 1.0
    if B == 0:
        return 0.0

    # dp[b] will store the probability for the current r
    # Initialize for r = 0: P(0, b) = 1.0 for all b > 0
    dp = [1.0] * (B + 1)
    # P(0, 0) is technically undefined in the game rules,
    # but based on the win condition (all same color),
    # we treat R=0 as a Black win.

    # Iterate through even red card counts from 2 to R
    for r in range(2, R + 1, 2):
        # Base case for each row: P(r, 0) = 0.0 (No black cards left)
        dp[0] = 0.0

        for b in range(1, B + 1):
            # Effective transition probabilities:
            # denom = (r - 1) + 2*b
            # P(r, b) = [(r-1)/denom * P(r-2, b)] + [2b/denom * P(r, b-1)]

            denom = (r - 1) + 2 * b
            p_red_reduced = (r - 1) / denom
            p_black_reduced = (2 * b) / denom

            # dp[b] currently holds P(r-2, b) from the previous outer loop iteration
            # dp[b-1] currently holds P(r, b-1) from the current inner loop iteration
            dp[b] = (p_red_reduced * dp[b]) + (p_black_reduced * dp[b - 1])

    return dp[B]


print(solve_p_bottom_up(24960, 12345))
