def container_with_most_water(nums):
    res = 0
    left = 0
    right = len(nums) - 1
    while left < right:
        area = (right - left) * min(nums[left], nums[right])
        res = max(res, area)
        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1
    return res


nums = [5, 3, 1, 7, 2]
print(container_with_most_water(nums))
