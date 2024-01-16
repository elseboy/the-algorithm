import random


def sort_array(nums):
    if len(nums) <= 1:
        return nums

    index = random.randint(0, len(nums) - 1)
    pivot = nums[index]

    less = [x for x in nums if x < pivot]
    equal = [x for x in nums if x == pivot]
    greater = [x for x in nums if x > pivot]

    return sort_array(less) + equal + sort_array(greater)


nums = [5, 1, 1, 2, 0, 0]
print(sort_array(nums))
