def nextPermutation(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i == -1:
        nums.reverse()
        return
    print(nums)

    j = len(nums) - 1
    while nums[j] <= nums[i]:
        j -= 1

    print(i, j)
    nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1 :] = reversed(nums[i + 1 :])

    print(nums)


nums = [1, 2, 3]
nextPermutation(nums)
