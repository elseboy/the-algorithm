def meeting_room(intervals):
    start, end = [], []

    intervals.sort(key=lambda i: i[0])
    for i in range(len(intervals)):
        start.append(intervals[i][0])

    intervals.sort(key=lambda i: i[-1])
    for i in range(len(intervals)):
        end.append(intervals[i][-1])
    print(start)
    print(end)
    res, count = 0, 0
    i, j = 0, 0

    while i < len(start):
        if start[i] < end[j]:
            count += 1
            i += 1
        else:
            count -= 1
            j += 1

        res = max(res, count)

    return res


intervals = [(0, 30), (15, 20), (5, 10)]
print(meeting_room(intervals))
