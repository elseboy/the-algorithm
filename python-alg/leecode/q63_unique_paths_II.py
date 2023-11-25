def uniquePathsWithObstacles(nums):
    m, n = len(nums), len(nums[0])
    dp = [[0] * (n + 1) for r in range(m + 1)]

    dp[m - 1][n] = 1
    print(dp)

    for r in range(m - 1, -1, -1):
        for c in range(n - 1, -1, -1):
            if nums[r][c] == 1:
                dp[r][c] = 0
            else:
                down_value = dp[r + 1][c]
                right_value = dp[r][c + 1]
                dp[r][c] = down_value + right_value

    return dp[0][0]


nums = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(uniquePathsWithObstacles(nums))
