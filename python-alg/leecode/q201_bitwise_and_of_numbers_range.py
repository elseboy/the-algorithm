def rangeBitwiseAnd(left, right):
    shift = 0

    while left < right:
        left >>= 1
        right >>= 1
        print(left, right)
        shift += 1
    return left << shift


left = 5
right = 7
print(rangeBitwiseAnd(left, right))
