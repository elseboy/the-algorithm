def two_sum(nums, target):
    n = len(nums) - 1
    l, r = 0, n

    while l <= r:
        if nums[l] + nums[r] == target:
            return [l + 1, r + 1]
        elif nums[l] + nums[r] > target:
            r -= 1
        else:
            l += 1
    return []


nums = [2, 3, 4]
target = 6
print(two_sum(nums, target))
