def romanToInt(s):
    val_map = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }
    result = 0
    i = 0

    while i < len(s):
        c = s[i : i + 2]
        if c in val_map:
            result += val_map[c]
            i += 2
        else:
            c = s[i : i + 1]
            result += val_map[c]
            i += 1

    return result


s = "MCMXCIV"
print(romanToInt(s))
