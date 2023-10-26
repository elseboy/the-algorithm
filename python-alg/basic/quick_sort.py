def quick_sort(arr, left_index, right_index):
    if left_index >= right_index:
        return
    pivot = arr[right_index]
    left_pointer = left_index
    right_pointer = right_index

    while left_pointer < right_pointer:
        while arr[left_pointer] <= pivot and left_pointer < right_pointer:
            left_pointer += 1
        while arr[right_pointer] >= pivot and left_pointer < right_pointer:
            right_pointer -= 1
        arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]

    meet_pointer = right_pointer
    arr[meet_pointer], arr[right_index] = arr[right_index], arr[meet_pointer]
    quick_sort(arr, left_index, left_pointer - 1)
    quick_sort(arr, left_pointer + 1, right_index)


my_list = [38, 27, 43, 3, 9, 82, 10]
quick_sort(my_list, 0, len(my_list) - 1)
print(my_list)
