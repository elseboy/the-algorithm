def length_of_LIS(nums):
    LIS = [1] * len(nums)
    print(LIS)

    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])

    print(LIS)
    return max(LIS)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(length_of_LIS(nums))
