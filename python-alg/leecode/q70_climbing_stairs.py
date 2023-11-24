def climbing_stairs(stairs):
    p, q, r = 0, 0, 1
    for i in range(1, stairs + 1):
        p = q
        q = r
        r = p + q
    return r


def dp_solution(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[n])


stairs = 5
print(climbing_stairs(stairs))
print(dp_solution(stairs))
