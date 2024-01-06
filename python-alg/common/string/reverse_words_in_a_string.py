def reverseWords(s):
    res = []
    end = len(s)

    for i in range(len(s) - 1, -1, -1):
        if s[i] == " ":
            end = i
        elif i == 0 or s[i - 1] == " ":
            if res:
                res.append(" ")
            res.append(s[i:end])

    return "".join(res)


s = "the sky is blue"
print(reverseWords(s))
