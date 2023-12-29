def maxProfit(prices):
    profit = 0
    min_price = prices[0]

    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            profit = max(profit, price - min_price)
                    
    return profit



prices = [7,1,5,3,6,4]
print(maxProfit(prices))
