def permute(nums):

    def backtrack(start, path):
        if start == len(nums):
            res.append(path.copy())
            return 

        for i in range(len(nums)):
            if nums[i] not in path:
                path.append(nums[i])
                backtrack(start + 1, path)
                path.pop()

    res = []
    backtrack(0, [])            
    return res


nums = [1,2,3]
print(permute(nums))
