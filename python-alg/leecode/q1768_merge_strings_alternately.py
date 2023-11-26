def mergeAlternately(word1, word2):
    merge = ""
    index = 0
    m, n = len(word1), len(word2)
    while word1 and word2 and index < min(m, n):
        merge += (word1[index] + word2[index])
        index += 1

    if index == m:
        merge += word2[index:]
    if index == n:
        merge += word1[index:]

    return merge


word1 = "ab"
word2 = "pqr"
print(mergeAlternately(word1, word2))
