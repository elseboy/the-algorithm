def combination(candidates, target):
    def backtrack(start, target, path):
        if target < 0:
            return
        if target == 0:
            res.append(path.copy())
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, target - candidates[i], path)
            path.pop()

    res = []
    candidates.sort()
    backtrack(0, target, [])

    return res


canidates = [2, 3, 6, 7]
target = 7
print(combination(canidates, target))
