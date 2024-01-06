def restoreIpAddresses(s):
    def backtrack(start, path):
        if len(path) == 4:
            if start == len(s):
                res.append('.'.join(path))

        for end in range(start + 1, min(start + 4, len(s) + 1)):
            segment = s[start:end]

            if 0 <= int(segment) <= 255 and (len(segment) == 1 or segment[0] != '0'):
                backtrack(end, path + [segment])

    res = []
    backtrack(0, [])

    return res


s = "101023"
print(restoreIpAddresses(s))
