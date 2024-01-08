def meeting_rooms(intervals):
    intervals.sort(key=lambda i: i[0])

    for i in range(1, len(intervals)):
        prev = intervals[i - 1]
        curr = intervals[i]

        if prev[-1] > curr[0]:
            return False

    return True


intervals1 = [(0, 30), (15, 20), (5, 10)]
intervals2 = [(5, 8), (9, 15)]

print(meeting_rooms(intervals1))
print(meeting_rooms(intervals2))
