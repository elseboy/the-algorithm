from collections import deque


def rotting_oranges(grid):
    queue = deque()
    time, fresh = 0, 0

    ROWS, COLS = len(grid), len(grid[0])
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                queue.append([r, c])
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    while queue and fresh > 0:
        for i in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if (
                    row < 0
                    or row == len(grid)
                    or col < 0
                    or col == len(grid[0])
                    or grid[row][col] != 1
                ):
                    continue
                grid[row][col] = 2
                queue.append([row, col])
                fresh -= 1
        time += 1

    return time if fresh == 0 else -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

print(rotting_oranges(grid))
