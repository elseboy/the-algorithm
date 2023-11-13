def minSubArrayLen(nums, target):
    l = total = 0
    result = len(nums) + 1

    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            window_size = (r - l) + 1
            result = min(result, window_size)
            total -= nums[l]
            l += 1

    return result if result != len(nums) + 1 else 0


nums = [2, 3, 1, 2, 4, 3]
target = 7

print(minSubArrayLen(nums, target))
