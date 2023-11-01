def sub_array_sum(nums, k):
    count = 0
    for i in range(len(nums)):
        _sum = 0
        for j in range(i, -1, -1):
            _sum += nums[j]
            if _sum == k:
                count += 1
    return count


nums = [1, 2, 3]
k = 3

print(sub_array_sum(nums, k))
