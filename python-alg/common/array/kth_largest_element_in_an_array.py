def quick_select(nums, k):
    k = len(nums) - k

    def quickSelect(l, r):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1

        nums[p], nums[r] = nums[r], nums[p]

        if k < p:
            return quickSelect(l, p - 1)
        elif k > p:
            return quickSelect(p + 1, r)
        else:
            return nums[p]

    return quickSelect(0, len(nums) - 1)


def min_heap(nums, k):
    return


nums = [3, 2, 1, 5, 6, 3, 4]
k = 2
print(quick_select(nums, k))
print(min_heap(nums, k))
