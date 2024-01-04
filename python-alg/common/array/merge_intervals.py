def merge(list):
    list.sort(key=lambda i: i[0])
    output = [list[0]]

    for start, end in list[1:]:
        lastEnd = output[-1][1]

        if start <= lastEnd:
            output[-1][1] = max(lastEnd, end)
        else:
            output.append([start, end])

    return output


list = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(list))
