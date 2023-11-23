def plusOne(digits):
    s = ""
    s += "".join(str(num) for num in digits)

    s = str(int(s) + 1)
    digits = [int(char) for char in s]
    return digits


digits = [9, 9]
print(plusOne(digits))
