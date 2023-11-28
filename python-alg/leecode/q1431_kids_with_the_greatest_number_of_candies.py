def kidsWithCandies(candies, extraCandies):
    biggest = max(candies)
    for i in range(len(candies)):
        if candies[i] + extraCandies >= biggest:
            candies[i] = True
        else:
            candies[i] = False
    return candies


candies = [12, 1, 12]
extraCandies = 10
print(kidsWithCandies(candies, extraCandies))
