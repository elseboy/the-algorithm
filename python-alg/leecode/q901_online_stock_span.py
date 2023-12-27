class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        
        self.stack.append((price, span))

        return span


stockSpanner = StockSpanner()

# Call next for each price
print(stockSpanner.next(100))  # Output: 1
print(stockSpanner.next(80))   # Output: 1
print(stockSpanner.next(60))   # Output: 1
print(stockSpanner.next(70))   # Output: 2
print(stockSpanner.next(60))   # Output: 1
print(stockSpanner.next(75))   # Output: 4
print(stockSpanner.next(85))   # Output: 6



