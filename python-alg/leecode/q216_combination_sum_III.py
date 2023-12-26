def combinationSum3(k, n):

    def backtrack(start, k, n, path, result):
        if k == 0 and n == 0:
            result.append(path.copy())
            return 
        if k == 0 or n == 0:
            return 

        for i in range(start, 10):
            path.append(i)
            backtrack(i + 1, k - 1, n - i, path, result)
            path.pop()

    result = []
    backtrack(1, k, n, [], result)
    return result



k = 3
n = 7
print(combinationSum3(k, n))
