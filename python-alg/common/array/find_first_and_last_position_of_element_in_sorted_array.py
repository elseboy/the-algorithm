def searchRange(nums, target):
    def search_left(nums, target):
        l, r = 0, len(nums) - 1
        res = -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                res = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return res

    def search_right(nums, target):
        l, r = 0, len(nums) - 1
        res = -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                res = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return res

    return [search_left(nums, target), search_right(nums, target)]


nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))
