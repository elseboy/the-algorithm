def convert(s, numRows):
    if numRows == 1:
        return s

    res = ""
    for r in range(numRows):
        incre = 2 * (numRows - 1)
        for i in range(r, len(s), incre):
            res += s[i]
            if r > 0 and r < numRows - 1 and i + incre - 2 * r < len(s):
                res += s[i + incre - 2 * r]

    return res


s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))
