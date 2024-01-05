def jump(nums):
    r = len(nums) - 1

    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= r:
            r = i

    return r == 0


nums = [2, 4, 1, 0, 4]
print(jump(nums))
