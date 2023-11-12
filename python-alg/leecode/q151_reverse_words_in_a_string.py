def reverseWords(s):
    words = s.split()
    reversed_words = words[::-1]
    reversed_string = " ".join(reversed_words)
    return reversed_string


s = "  hello world  "
print(reverseWords(s))
