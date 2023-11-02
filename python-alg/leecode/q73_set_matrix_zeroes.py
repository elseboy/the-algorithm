def set_matrix_zeroes(matrix):
    row, col = len(matrix), len(matrix[0])
    row_zero = set()
    col_zero = set()

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                row_zero.add(i)
                col_zero.add(j)

    print(matrix)

    for i in range(row):
        for j in range(col):
            if i in row_zero or j in col_zero:
                matrix[i][j] = 0

    return matrix


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(set_matrix_zeroes(matrix))
