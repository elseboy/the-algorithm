from collections import Counter, defaultdict


def equalPairs(grid):
    count = Counter(tuple(row) for row in grid)
    return sum(count[col] for col in zip(*grid))


grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
print(equalPairs(grid))
