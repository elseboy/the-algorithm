def longestPalindrome(s):
    result = ""
    resLen = 0

    for i in range(len(s)):
        # odd length
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                result = s[l : r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1

        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                result = s[l : r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1

    return result


s = "babad"
print(longestPalindrome(s))
