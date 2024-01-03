def decode_ways(s):
    n = len(s)

    dp = [0] * (n + 1)

    dp[0] = 1
    dp[1] = 0 if s[0] == '0' else 1

    for i in range(2, n + 1):
        if 1 <= int(s[i - 1]) <= 9:
            dp[i] += dp[i - 1]

        two_digits = int(s[i - 2:i])
        if 10 <= two_digits <= 26:
            dp[i] += dp[i - 2]

    return dp[n]


s = '226'
print(decode_ways(s))
