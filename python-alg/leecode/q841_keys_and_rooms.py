def canVisitAllRooms(rooms):
    n = len(rooms)
    visited = set()

    def dfs(room):
        visited.add(room)
        for key in rooms[room]:
            if key not in visited:
                dfs(key)

    dfs(0)
    return len(visited) == n


rooms = [[1], [2], [3], []]
print(canVisitAllRooms(rooms))
