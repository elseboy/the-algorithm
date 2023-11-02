def merge_intervals(arrs):
    n = len(arrs)
    result = []
    arrs.sort(key=lambda x: x[0])
    result = [arrs[0]]

    for i in range(1, n):
        curr = arrs[i]
        prev = result[-1]
        if curr[0] <= prev[1]:
            prev[1] = max(prev[1], curr[1])
        else:
            result.append(curr)
    return result


arrs = [[1, 4], [5, 6]]
print(merge_intervals(arrs))
