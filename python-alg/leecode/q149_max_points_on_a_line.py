from collections import defaultdict


def my_gcd(a, b):
    return a if b == 0 else my_gcd(b, a % b)


def slope_reduce(a, b):
    common_divisor = my_gcd(a, b)
    return (a // common_divisor, b // common_divisor)


def maxPoints(points):
    ans = 1

    for i in range(len(points)):
        point_map = {}
        max_points = 0

        for j in range(i + 1, len(points)):
            delta_x = points[i][0] - points[j][0]
            delta_y = points[i][1] - points[j][1]

            reduced_solpe = slope_reduce(delta_x, delta_y)
            print(reduced_solpe)

            point_map[reduced_solpe] = point_map.get(reduced_solpe, 0) + 1
            max_points = max(max_points, point_map[reduced_solpe])

        ans = max(ans, max_points + 1)

    return ans


points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
print(maxPoints(points))
