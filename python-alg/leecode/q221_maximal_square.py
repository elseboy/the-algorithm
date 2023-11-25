def maximalSquare(matrix):
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    max_side = 0

    for i in dp:
        print(i)

    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            if matrix[i][j] == "1":
                top_left = dp[i + 1][j + 1]
                top = dp[i + 1][j]
                left = dp[i][j + 1]

                dp[i][j] = min(top_left, top, left) + 1
                max_side = max(max_side, dp[i][j])
    return max_side * max_side


matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
print(maximalSquare(matrix))
