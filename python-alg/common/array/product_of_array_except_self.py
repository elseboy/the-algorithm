def productExceptSelf(nums):
    n = len(nums)
    prefix, postfix = [1] * n, [1] * n
    prefix[0] = nums[0]
    postfix[n - 1] = nums[n - 1]

    res = []

    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i]

    for i in range(n - 2, -1, -1):
        postfix[i] = postfix[i + 1] * nums[i]

    print(prefix)
    print(postfix)
    
    for i in range(n):
        if i == 0:
            res.append(postfix[i + 1])
        elif i == n - 1:
            res.append(prefix[i - 1])
        else:
            res.append(prefix[i - 1] * postfix[i + 1])
            
    return res


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
