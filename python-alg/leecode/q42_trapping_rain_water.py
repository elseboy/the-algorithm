def trapping_rain_water(nums):
    n = len(nums)
    left = 0
    right = n - 1
    left_max = nums[left]
    right_max = nums[right]
    trapped_water = 0
    while left < right:
        if nums[left] < nums[right]:
            if nums[left] >= left_max:
                left_max = nums[left]
            else:
                trapped_water += left_max - nums[left]
            left += 1
        else:
            if nums[right] >= right_max:
                right_max = nums[right]
            else:
                trapped_water += right_max - nums[right]
            right -= 1
    return trapped_water


nums = [4, 2, 0, 3, 2, 5]
print(trapping_rain_water(nums))
