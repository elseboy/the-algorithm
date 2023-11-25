def isInterleave(s1, s2, s3):
    l1, l2, l3 = len(s1), len(s2), len(s3)

    if l1 + l2 != l3:
        return False

    dp = [[False] * (l2 + 1) for _ in range(l1 + 1)]
    dp[l1][l2] = True
    print(dp)

    for i in range(l1, -1, -1):
        for j in range(l2, -1, -1):
            if i < l1 and s1[i] == s3[i + j] and dp[i + 1][j]:
                dp[i][j] = True
            if j < l2 and s2[j] == s3[i + j] and dp[i][j + 1]:
                dp[i][j] = True

    print(dp)
    return dp[0][0]


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(isInterleave(s1, s2, s3))
