def intToRoman(num):
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

    res = ""

    reversed_items = list(reversed(val_map.items()))
    for k, v in reversed_items:
        if num // v:
            count = num // v
            res += k * count
            num = num % v

    return res


num = 58
print(intToRoman(num))
