def rotate_image(matrix):
    left, right = 0, len(matrix) - 1
    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            # save the first top value
            # do it in reverse order, youtobe
            top_left = matrix[top][left + i]

            # move bottom left into top left
            matrix[top][left + i] = matrix[bottom - i][left]

            # move bottom right into bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # move top right into bottom right
            matrix[bottom][right - i] = matrix[top + i][right]

            # move top left into top right
            matrix[top + i][right] = top_left

        right -= 1
        left += 1

    return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate_image(matrix))
