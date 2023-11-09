def partitionLabels(s):
    lastIndex = {}  # map every char
    for i, c in enumerate(s):
        lastIndex[c] = i

    print(s)
    print(lastIndex)

    result = []
    size, end = 0, 0
    for i, c in enumerate(s):
        size += 1
        end = max(end, lastIndex[c])

        if i == end:
            result.append(size)
            size = 0

    return result


s = "ababcbacadefegdehijhklij"
print(partitionLabels(s))
