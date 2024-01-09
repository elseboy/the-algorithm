def rotate_image(matrix):
    l, r = 0, len(matrix[0]) - 1

    while l < r:
        for i in range(r - l):
            top, bottom = l, r

            topLeft = matrix[top][l + i]

            matrix[top][l + i] = matrix[bottom - i][l]

            matrix[bottom - i][l] = matrix[bottom][r - i]

            matrix[bottom][r - i] = matrix[top + i][r]

            matrix[top + i][r] = topLeft

        r -= 1
        l += 1

    return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate_image(matrix))
