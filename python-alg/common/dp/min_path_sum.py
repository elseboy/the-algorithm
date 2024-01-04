def minPathSum(grid):
    rows, cols = len(grid), len(grid[0])

    dp = [[float('inf')] * (cols + 1) for _ in range(rows + 1)]

    dp[rows - 1][cols] = 0
    dp[rows][cols - 1] = 0

    for r in range(rows - 1, -1, -1):
        for c in range(cols - 1, -1, -1):
            curr = grid[r][c]
            down = dp[r + 1][c]
            right = dp[r][c + 1]

            dp[r][c] = curr + min(down, right)
    
    return dp[0][0] 


grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum(grid))
