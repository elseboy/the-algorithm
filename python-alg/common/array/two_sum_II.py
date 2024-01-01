def twoSum(nums, target):
    l, r = 0, len(nums) - 1

    while l < r:
        total = nums[l] + nums[r]

        if total == target:
            return [l + 1, r + 1]
        elif total > target:
            r -= 1
        else:
            l += 1 

    return []


nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
