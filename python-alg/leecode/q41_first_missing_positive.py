def first_missing_positive(nums):
    n = len(nums)

    for i in range(n):
        while nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            temp = nums[nums[i] - 1]
            nums[nums[i] - 1] = nums[i]
            nums[i] = temp

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


nums = [7, 8, 9, 11, 12]
print(first_missing_positive(nums))
