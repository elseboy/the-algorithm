def generate(rows):
    dp = [[0] * rows for _ in range(rows)]

    dp[0][0] = 1

    for i in range(1, rows):
        dp[i][0] = 1

        for j in range(1, i + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    result = [[dp[i][j] for j in range(i + 1)] for i in range(rows)]
    return result


rows = 5
print(generate(rows))
