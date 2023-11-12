def hIndex(citations):
    citations = sorted(citations, reverse=True)

    max_index = 0
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            max_index += 1

    return max_index


citations = [3, 0, 6, 1, 5]
print(hIndex(citations))
