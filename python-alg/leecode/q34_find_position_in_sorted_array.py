def search_range(nums, target):
    l, r = 0, len(nums) - 1
    result = [-1, -1]

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            result[0] = mid
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            result[1] = mid
            l = mid + 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return result


nums = [5, 7, 7, 8, 8, 10]
target = 8

print(search_range(nums, target))
