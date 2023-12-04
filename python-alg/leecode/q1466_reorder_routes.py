def minReorder(connections, n):
    graph = {i: [] for i in range(n)}
    roads_to_reverse = 0
    print(graph)

    for a, b in connections:
        graph[a].append((b, 1))  # 1 forward
        graph[b].append((a, 0))  # 0 backward

    print(graph)

    visited = set()

    def dfs(city):
        nonlocal roads_to_reverse
        visited.add(city)

        for neighbor, direction in graph[city]:
            if neighbor not in visited:
                roads_to_reverse += direction
                dfs(neighbor)

    dfs(0)
    return roads_to_reverse


n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
print(minReorder(connections, n))
