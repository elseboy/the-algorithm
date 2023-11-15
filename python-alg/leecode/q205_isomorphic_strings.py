def isIsomorphic(s, t):
    s_to_t = {}
    t_to_s = {}

    for i in range(len(s)):
        s_char, t_char = s[i], t[i]

        if s_char in s_to_t:
            if s_to_t[s_char] != t_char:
                return False
        else:
            s_to_t[s_char] = t_char

        if t_char in t_to_s:
            if t_to_s[t_char] != s_char:
                return False
        else:
            t_to_s[t_char] = s_char

    return True


s = "egg"
t = "add"
print(isIsomorphic(s, t))
