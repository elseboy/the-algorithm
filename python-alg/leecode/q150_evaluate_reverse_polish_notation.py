def evalRPN(tokens):
    stack = []

    for token in tokens:
        if token.isdigit() or (token[0] == "-" and token[1:].isdigit()):
            stack.append(int(token))
        else:
            t1 = stack.pop()
            t2 = stack.pop()

            if token == "+":
                stack.append(t1 + t2)
            elif token == "-":
                stack.append(t1 - t2)

            elif token == "*":
                stack.append(t1 * t2)

            elif token == "/":
                stack.append(int(t1 + t2))

    return stack.pop()


tokens = ["2", "1", "+", "3", "*"]
print(evalRPN(tokens))
