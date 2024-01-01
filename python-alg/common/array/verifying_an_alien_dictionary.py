def isAlienSorted(words, order):
    order_dict = {c: i for i, c in enumerate(order)}

    def compare_words(word1, word2):
        len1, len2 = len(word1), len(word2)

        for i in range(min(len1, len2)):
            if word1[i] != word2[i]:
                return order_dict[word1[i]] - order_dict[word2[i]]
        return len1 - len2

    for i in range(1, len(words)):
        if compare_words(words[i - 1], words[i]) > 0:
            return False

    return True


words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(isAlienSorted(words, order))
