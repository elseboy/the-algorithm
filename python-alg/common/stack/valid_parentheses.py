def valid(s):
    dic = {"{": "}", "[": "]", "(": ")"}
    stack = ["?"]

    for c in s:
        if c in dic:
            stack.append(c)
        else:
            temp = stack.pop()
            if c != dic[temp]:
                return False

    return len(stack) == 1


s = "()[]{}"
print(valid(s))
