def calculate(s: str) -> int:
    stack = []
    operand = 0
    result = 0  # For the final result
    sign = 1  # 1 represents positive, -1 represents negative

    for char in s:
        if char.isdigit():
            operand = operand * 10 + int(char)
        elif char == "+":
            result += sign * operand
            sign = 1  # Update the sign for the next operand
            operand = 0
        elif char == "-":
            result += sign * operand
            sign = -1  # Update the sign for the next operand
            operand = 0
        elif char == "(":
            stack.append((result, sign))
            result = 0
            sign = 1
        elif char == ")":
            result += sign * operand
            operand = 0
            prev_result, prev_sign = stack.pop()
            result = prev_result + prev_sign * result

    return result + sign * operand


s = "(1+(4+5+2)-3)+(6+8)"
print(calculate(s))
