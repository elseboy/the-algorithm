def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
                
    return max(dp)


nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))
