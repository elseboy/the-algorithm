def move_zeroes(nums):
    index = 0
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1
        else:
            count += 1
    start_index = max(0, len(nums) - count)
    for i in range(start_index, len(nums)):
        nums[i] = 0

    return nums


nums = [1, 0, 1]
move_zeroes(nums)
print(nums)
