def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    len_gcd = gcd(len(str1), len(str2))
    return str1[:len_gcd]


str1 = "ABCABC"
str2 = "ABC"

print(gcdOfStrings(str1, str2))
