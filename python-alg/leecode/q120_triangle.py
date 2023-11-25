def minimumTotal(nums):
    if not nums:
        return 0

    for i in range(len(nums) - 2, -1, -1):
        for j in range(len(nums[i])):
            curr_value = nums[i][j]
            print(" " + str(curr_value))
            down_left = nums[i + 1][j]
            down_right = nums[i + 1][j + 1]
            print(down_left, down_right)

            nums[i][j] = curr_value + min(down_left, down_right)

    return nums[0][0]


nums = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(minimumTotal(nums))
