def removeDuplicates(nums):
    count = 1

    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            nums[count] = nums[i + 1]
            count += 1

    return count


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))
