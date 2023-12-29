1. Two Sum:

   Use map to reduce one layer loop, if diff not exits in map, then add it to map, this can make sure duplicate elements like [3, 3] will not return [0, 0].

2. Best time to but and sell stock I

   Assume the first element is min price, then loop the rest to compare, if it is smaller, then update min price to current, do minus if the current price is bigger than min price.