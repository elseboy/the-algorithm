def maxProfit(prices, fee):
    n = len(prices)
    dp = [[0, 0] for _ in range(n)]
    dp[0][1] = -prices[0] - fee

    for i in range(1, n):
        # Option 1: Do nothing on day i (same as the previous day)
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        # Option 2: Sell the stock bought on the previous day
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)

    return dp[-1][0]


# Example usage:
prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(maxProfit(prices, fee))
