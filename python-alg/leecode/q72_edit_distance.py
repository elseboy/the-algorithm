def min_distance(w1, w2):
    cache = [[float("inf")] * (len(w2) + 1) for i in range(len(w1) + 1)]
    print(cache)

    for j in range(len(w2) + 1):
        cache[len(w1)][j] = len(w2) - j
    print(cache)

    for i in range(len(w1) + 1):
        cache[i][len(w2)] = len(w1) - i
    print(cache)

    for i in range(len(w1) - 1, -1, -1):
        for j in range(len(w2) - 1, -1, -1):
            if w1[i] == w2[j]:
                cache[i][j] = cache[i + 1][j + 1]
            else:
                cache[i][j] = 1 + min(
                    cache[i + 1][j], cache[i][j + 1], cache[i + 1][j + 1]
                )

    return cache[0][0]


w1 = "horse"
w2 = "ros"
print(min_distance(w1, w2))
