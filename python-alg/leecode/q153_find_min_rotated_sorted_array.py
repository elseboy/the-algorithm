def find_min_in_rotated_sorted_array(nums):
    result = nums[0]
    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l] < nums[r]:
            result = min(result, nums[l])
            break

        mid = (l + r) // 2
        result = min(result, nums[mid])
        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid - 1

    return result


nums = [3, 4, 5, 1, 2]
print(find_min_in_rotated_sorted_array(nums))
