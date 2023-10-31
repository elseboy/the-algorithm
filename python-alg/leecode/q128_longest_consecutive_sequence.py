def longest_sequence(nums):
    nums_set = set(nums)
    longest = 0
    for num in nums:
        if num - 1 not in nums_set:
            curr_num = num
            curr_len = 1
            while curr_num + 1 in nums_set:
                curr_num += 1
                curr_len += 1
            longest = max(longest, curr_len)
    return longest


nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
print(longest_sequence(nums))
