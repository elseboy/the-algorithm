def max_profit(prices):
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        min_price = min(price, min_price)
        max_profit = max(price - min_price, max_profit)
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))
