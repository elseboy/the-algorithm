def remove_element(nums, val):
    length = 0

    for num in nums:
        if num != val:
            nums[length] = num
            length += 1

    return length


nums = [3, 2, 2, 3]
val = 3
print(remove_element(nums, val))
