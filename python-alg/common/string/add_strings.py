def add_strings(s1, s2):
    res = []
    carry = 0

    i, j = len(s1) - 1, len(s2) - 1

    while i >= 0 or j >= 0 or carry > 0:
        x = int(s1[i]) if i >= 0 else 0
        y = int(s2[j]) if j >= 0 else 0

        total = x + y + carry
        carry = total // 10
        digit = total % 10

        res.insert(0, str(digit))

        i -= 1
        j -= 1

    return ''.join(res)


s1 = '0'
s2 = '0'
print(add_strings(s1, s2))
