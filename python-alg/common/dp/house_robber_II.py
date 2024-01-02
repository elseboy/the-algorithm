def rob(nums):
    if len(nums) == 1:
        return nums[0]

    def rob_I(nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]

    rob_left = rob_I(nums[:-1])
    rob_right = rob_I(nums[1:])

    return max(rob_left, rob_right)


nums = [2, 3, 2]
print(rob(nums))
