def remove_duplicates(nums):
    length = 2

    print(nums)

    for i in range(2, len(nums)):
        if nums[i] != nums[length - 2]:
            nums[length] = nums[i]
            length += 1

    print(nums)
    return length


nums = [1, 1, 1, 2, 2, 3]
print(remove_duplicates(nums))
