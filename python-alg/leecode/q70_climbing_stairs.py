def climbing_stairs(stairs):
    p, q, r = 0, 0, 1
    for i in range(1, stairs + 1):
        p = q
        q = r
        r = p + q
    return r


stairs = 3
print(climbing_stairs(stairs))
