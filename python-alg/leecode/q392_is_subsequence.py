def vaild(s, t):
    i, j = 0, 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            print(i)
            i += 1
        j += 1

    return i == len(s)


s = "abc"
t = "ahbgdc"
print(vaild(s, t))
