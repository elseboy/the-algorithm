def two_sum(nums, target):
    num_map = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_map:
            return [num_map[diff], i]

        num_map[num] = i  
    
    return None

nums = [3, 2, 4]
target = 6
print(two_sum(nums, target))
