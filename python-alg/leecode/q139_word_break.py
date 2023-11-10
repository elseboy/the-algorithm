def word_break(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True
    print(dp)

    for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
            if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break

    print(dp)
    return dp[0]


s = "leetcode"
wordDict = ["leet", "code"]
print(word_break(s, wordDict))
