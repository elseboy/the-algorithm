from collections import deque


def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    wordList = set(wordList)
    queue = deque([(beginWord, 1)])

    while queue:
        curr_word, trans = queue.popleft()

        if curr_word == endWord:
            return trans

        for i in range(len(curr_word)):
            for char in "abcdefghijklmnopqrstuvwxyz":
                next_word = curr_word[:i] + char + curr_word[i + 1 :]

                if next_word in wordList:
                    wordList.remove(next_word)
                    queue.append((next_word, trans + 1))
    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(ladderLength(beginWord, endWord, wordList))
