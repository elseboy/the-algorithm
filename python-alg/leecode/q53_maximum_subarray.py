def max_sub_array(nums):
    curr_sum = 0
    max_sum = float("-inf")

    for num in nums:
        curr_sum = max(curr_sum + num, num)
        max_sum = max(curr_sum, max_sum)
    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sub_array(nums))
