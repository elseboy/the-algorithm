def rob(nums):
    rob1, rob2 = 0, 0

    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp

    return rob2


def dp_solution(nums):
    dp = [0] * len(nums)

    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        print(dp)

    return dp[-1]


nums = [2, 7, 9, 3, 1]
print(dp_solution(nums))
