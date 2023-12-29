def containsDuplicate(nums):
    num_set = set(nums)
    return True if len(nums) != len(num_set) else False


nums = [1, 2, 3]
print(containsDuplicate(nums))
