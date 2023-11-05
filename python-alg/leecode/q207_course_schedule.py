from collections import deque


def course_schedule(num_course, arr):
    preMap = {i: [] for i in range(num_course)}
    for crs, pre in arr:
        preMap[crs].append(pre)

    visitSet = set()

    def dfs(crs):
        if crs in visitSet:
            return False
        if preMap[crs] == []:
            return True

        visitSet.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre):
                return False

        visitSet.remove(crs)
        preMap[crs] = []
        return True

    for crs in range(num_course):
        if not dfs(crs):
            return False

    return True


arr = [[1, 0]]
num_course = 2
print(course_schedule(num_course, arr))
