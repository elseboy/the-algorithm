from collections import Counter


def find_anagram(s, p):
    result = []
    p_counter = Counter(p)
    s_counter = Counter(s[: len(p)])

    for i in range(len(p), len(s)):
        if s_counter == p_counter:
            result.append(i - len(p))

        s_counter[s[i]] += 1

        if s_counter[s[i - len(p)]] == 1:
            del s_counter[s[i - len(p)]]
        else:
            s_counter[s[i - len(p)]] -= 1

    if s_counter == p_counter:
        result.append(len(s) - len(p))

    return result


st = "cbaebabacd"
pt = "abc"
print(find_anagram(st, pt))
