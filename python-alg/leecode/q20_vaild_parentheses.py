def vaild_parentheses(char):
    dic = {"{": "}", "[": "]", "(": ")", "?": "?"}
    stack = ["?"]
    for c in char:
        if c in dic:
            stack.append(c)
        else:
            temp = stack.pop()
            if c != dic[temp]:
                return False
    return True


char = "()"
print(vaild_parentheses(char))
