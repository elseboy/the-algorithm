def find_largest(nums, k):
    k = len(nums) - k

    def quick_sort(l, r):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]

        if p > k:
            return quick_sort(l, p - 1)
        elif p < k:
            return quick_sort(p + 1, r)
        else:
            return nums[p]

    return quick_sort(0, len(nums) - 1)


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]

k = 4

print(find_largest(nums, k))
