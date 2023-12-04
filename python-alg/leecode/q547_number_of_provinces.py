def findCircleNum(isConnected):
    def dfs(city):
        visited.add(city)
        for neighbor in range(n):
            if isConnected[city][neighbor] == 1 and neighbor not in visited:
                dfs(neighbor)

    n = len(isConnected)
    provinces = 0
    visited = set()

    for city in range(n):
        if city not in visited:
            dfs(city)
            provinces += 1

    return provinces


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(findCircleNum(isConnected))
