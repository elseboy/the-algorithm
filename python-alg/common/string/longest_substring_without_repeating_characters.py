def lengthOfLongestSubstring(s):
    chars = set()
    count = 0
    res = 0

    for i in range(len(s)):
        while s[i] in chars:
            chars.remove(s[count])
            count += 1
        chars.add(s[i])
        res = max(res, i - count + 1)

    return res


s = "bacabcbb"
print(lengthOfLongestSubstring(s))
