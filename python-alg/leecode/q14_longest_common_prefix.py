def longestCommonPrefix(s):
    prefix = min(s, key=len)

    for i in range(len(prefix)):
        for word in s:
            if prefix[i] != word[i]:
                return prefix[:i]

    return prefix


s = ["ab", "a"]
print(longestCommonPrefix(s))
