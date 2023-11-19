def findOrder(numCourses, prerequisites):
    prereq = {i: [] for i in range(numCourses)}
    print(prereq)

    for crs, pre in prerequisites:
        prereq[crs].append(pre)
    print(prereq)

    output = []
    visit, cycle = set(), set()

    def dfs(crs):
        if crs in cycle:
            return False
        if crs in visit:
            return True

        cycle.add(crs)
        for pre in prereq[crs]:
            if dfs(pre) == False:
                return False

        cycle.remove(crs)
        visit.add(crs)
        output.append(crs)
        return True

    for c in range(numCourses):
        if dfs(c) == False:
            return []

    return output


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

print(findOrder(numCourses, prerequisites))
