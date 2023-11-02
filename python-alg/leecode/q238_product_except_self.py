def product_except_self(nums):
    n = len(nums)
    left_product = [1] * n
    right_product = [1] * n
    result = [1] * n

    left = 1
    right = 1

    for i in range(1, n):
        left *= nums[i - 1]
        left_product[i] = left

    for i in range(n - 2, -1, -1):
        right *= nums[i + 1]
        right_product[i] = right

    for i in range(n):
        result[i] = left_product[i] * right_product[i]

    return result


nums = [-1, 1, 0, -3, 3]
print(product_except_self(nums))
