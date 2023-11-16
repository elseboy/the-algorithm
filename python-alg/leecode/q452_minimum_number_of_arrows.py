def findMinArrowShots(points):
    points.sort(key=lambda x: x[1])

    arrow = 1
    end = points[0][1]

    for interval in points[1:]:
        start, curr_end = interval
        print(start, curr_end)

        if start <= end:
            continue

        end = curr_end
        arrow += 1

    return arrow


points = [
    [3, 9],
    [7, 12],
    [3, 8],
    [6, 8],
    [9, 10],
    [2, 9],
    [0, 9],
    [3, 9],
    [0, 6],
    [2, 8],
]
print(findMinArrowShots(points))
