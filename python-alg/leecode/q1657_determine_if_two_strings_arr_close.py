from collections import Counter


def closeStrings(word1, word2):
    if sorted(set(word1)) != sorted(set(word2)):
        return False

    freq1 = Counter(word1)
    freq2 = Counter(word2)

    return sorted(freq1.values()) == sorted(freq2.values())


word1 = "abc"
word2 = "bca"
print(closeStrings(word1, word2))
