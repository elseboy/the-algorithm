def longestCommonPrefix(strs):
    prefix = min(strs, key=len)

    for i in range(len(prefix)):
        for word in strs:
            if prefix[i] != word[i]:
                return prefix[:i]

    return prefix


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))
