def remove_duplicates(nums):
    length = 1

    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            nums[length] = nums[i + 1]
            length += 1

    return length


nums = [1, 1, 2, 2, 3]
print(remove_duplicates(nums))
