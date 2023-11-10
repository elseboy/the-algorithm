def max_product(nums):
    result = max(nums)
    currMin, currMax = 1, 1

    for n in nums:
        if n == 0:
            currMin = currMax = 1
            continue

        temp = currMax * n
        currMax = max(n * currMax, n * currMin, n)
        currMin = min(temp, n * currMin, n)

        result = max(result, currMax, currMin)

    return result


nums = [2, 3, -2, 4]
print(max_product(nums))
