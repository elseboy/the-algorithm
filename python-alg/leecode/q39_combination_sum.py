def combination_sum(cands, target):
    result = []

    def dfs(i, curr_val, total):
        if total == target:
            result.append(curr_val.copy())
            return
        if i >= len(cands) or total > target:
            return

        curr_val.append(cands[i])
        dfs(i, curr_val, total + cands[i])
        curr_val.pop()
        dfs(i + 1, curr_val, total)

    dfs(0, [], 0)
    return result


nums = [2, 3, 6, 7]
target = 7
print(combination_sum(nums, target))
