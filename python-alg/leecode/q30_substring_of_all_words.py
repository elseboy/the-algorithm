from collections import Counter


def findSubstring(s, words):
    word_len = len(words[0])
    total_len = word_len * len(words)
    result = []

    word_count = Counter(words)

    for i in range(word_len):
        left, right = i, i
        curr_count = Counter()

        print(i)
        while right + word_len <= len(s):
            word = s[right : right + word_len]
            right += word_len
            curr_count[word] += 1
            print(curr_count)

            while curr_count[word] > word_count[word]:
                left_word = s[left : left + word_len]
                left += word_len
                curr_count[left_word] -= 1

            if right - left == total_len:
                result.append(left)

    return result


s = "barfoofoobarthefoobarman"
words = ["bar", "foo", "the"]

print(findSubstring(s, words))
