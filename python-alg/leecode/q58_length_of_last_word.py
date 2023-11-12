def lengthOfLastWord(s):
    l, r = 0, len(s) - 1
    actual_went = 0

    while l < r:
        if s[r] == " ":
            r -= 1
        else:
            break

    if l == r:
        return 1

    while l <= r:
        if s[r] == " ":
            break
        r -= 1
        actual_went += 1

    return actual_went


s = "day"
print(lengthOfLastWord(s))
