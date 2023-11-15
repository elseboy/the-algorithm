from collections import Counter


def wordPattern(pattern, s):
    words = s.split()

    pattern_mapping = {}
    word_mapping = {}

    for char, word in zip(pattern, words):
        if char in pattern_mapping:
            if pattern_mapping[char] != word:
                return False
        else:
            pattern_mapping[char] = word

        if word in word_mapping:
            if word_mapping[word] != char:
                return False
        else:
            word_mapping[word] = char


pattern = "aaaa"
s = "dog cat cat dog"
print(wordPattern(pattern, s))
