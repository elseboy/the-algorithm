def letter_combinations(digits):
    result = []
    digitsToChar = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "qprs",
        "8": "tuv",
        "9": "wzyz",
    }

    def backtrack(i, curr_str):
        if len(curr_str) == len(digits):
            result.append(curr_str)
            return

        for c in digitsToChar[digits[i]]:
            backtrack(i + 1, curr_str + c)

    if digits:
        backtrack(0, "")

    return result


s = "23"
print(letter_combinations(s))
