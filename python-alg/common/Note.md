# Array

1. Two Sum:

   Use map to reduce one layer loop, if diff not exits in map, then add it to map, this can make sure duplicate elements like [3, 3] will not return [0, 0].

2. Best time to but and sell stock:

   Assume the first element is min price, then loop the rest to compare, if it is smaller, then update min price to current, do minus if the current price is bigger than min price.

3. Contains Duplicate:
   Pass
4. Contains Duplicate:
   Use a map to map the num and its' index, then check if it is duplicated in the map and its' index minus duplicate to make sure it is  smaller than k.