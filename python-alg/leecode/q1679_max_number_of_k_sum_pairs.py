def maxOperations(nums, k):
    count = {}
    operation = 0

    for num in nums:
        diff = k - num

        if diff in count and count[diff] > 0:
            count[diff] -= 1
            operation += 1
        else:
            count[num] = count.get(num, 0) + 1

    return operation


nums = [1, 2, 3, 4]
k = 5
print(maxOperations(nums, k))
