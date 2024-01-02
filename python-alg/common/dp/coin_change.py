def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)

    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


coins = [1, 3, 4, 5]
amount = 7
print(coinChange(coins, amount))
