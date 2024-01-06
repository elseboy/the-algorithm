def subsets(nums):
    def backtrack(start, path):
        res.append(path[:])

        if start == len(nums):
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue

            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    nums.sort()
    res = []
    backtrack(0, [])
    return res


nums = [1, 2, 3]
print(subsets(nums))
