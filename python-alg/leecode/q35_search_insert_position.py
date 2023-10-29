def search_insert_position(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


my_list = [3, 9, 10, 27, 38, 43, 82]
print(search_insert_position(my_list, 12))
