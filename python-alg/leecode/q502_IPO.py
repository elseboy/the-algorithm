import heapq


def findMaximizedCapital(k, W, Profits, Capital):
    projects = list(zip(Capital, Profits))
    print(projects)
    projects.sort(key=lambda x: x[0])  # Sort projects by capital
    print(projects)

    max_heap = []  # Max heap to store profits of available projects
    i = 0

    for _ in range(k):
        while i < len(projects) and projects[i][0] <= W:
            heapq.heappush(max_heap, -projects[i][1])
            i += 1

        print(max_heap)
        if max_heap:
            W -= heapq.heappop(max_heap)
        else:
            break

    return W


# Example usage:
k = 2
W = 0
Profits = [1, 2, 3]
Capital = [0, 1, 1]
result = findMaximizedCapital(k, W, Profits, Capital)
print(result)  # Output: 4
