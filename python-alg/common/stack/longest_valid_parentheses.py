def longest_valid_parentheses(s):
    stack = [-1]
    _max = 0

    for i, p in enumerate(s):
        if p == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                _max = max(_max, i - stack[-1])

    return _max


s = ")()())"
print(longest_valid_parentheses(s))
