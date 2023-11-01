def longest_substring(s):
    left, right = 0, 0
    length, max_length = 0, 0
    c_set = set()
    while right < len(s):
        if s[right] not in c_set:
            c_set.add(s[right])
            length += 1
            if length > max_length:
                max_length = length
            right += 1
        else:
            while s[right] in c_set:
                c_set.remove(s[left])
                left += 1
                length -= 1
            c_set.add(s[right])
            length += 1
            right += 1
    return max_length


s = "abcabcbb"
print(longest_substring(s))
