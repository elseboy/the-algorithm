from collections import Counter


def min_window(s, t):
    need, missing = Counter(t), len(t)
    i = start = end = 0

    for j, c in enumerate(s, 1):
        missing -= need[c] > 0
        need[c] -= 1

        if not missing:
            while need[s[i]] < 0:
                need[s[i]] += 1
                i += 1
            if not end or j - i < end - start:
                start, end = i, j
    return s[start:end]


s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s, t))
