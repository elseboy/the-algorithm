def search_matrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1

    while row < rows and col > 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1

    return False


matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]
target = 5
print(search_matrix(matrix, target))
