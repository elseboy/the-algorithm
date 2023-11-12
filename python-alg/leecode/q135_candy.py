def candy(ratings):
    N = len(ratings)
    can = [1 for _ in range(N)]

    print(can)

    for i in range(1, N):
        if ratings[i] > ratings[i - 1]:
            can[i] = can[i - 1] + 1

    print(can)

    for i in range(N - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            can[i] = max(can[i + 1] + 1, can[i])

    print(can)

    return sum(can)


ratings = [5, 3, 1, 4, 5, 2]
print(candy(ratings))
