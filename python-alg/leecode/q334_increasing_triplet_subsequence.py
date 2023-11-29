def increasingTriplet(nums):
    first = second = float('inf')
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True

    return False


nums = [5, 4, 3, 2, 1]
print(increasingTriplet(nums))
