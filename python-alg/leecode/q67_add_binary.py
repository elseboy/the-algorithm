def addBinary(a, b):
    res = []
    maxLength = max(len(a), len(b))
    carry = 0

    a = a.zfill(maxLength)
    b = b.zfill(maxLength)

    for i in range(maxLength - 1, -1, -1):
        bit_sum = int(a[i]) + int(b[i]) + carry
        print(a[i], b[i], bit_sum)
        res.insert(0, str(bit_sum % 2))
        carry = bit_sum // 2

    if carry:
        res.insert(0, str(carry))

    return "".join(res)


a = "11"
b = "1"
print(addBinary(a, b))
