def insertion_sort(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        j = i - 1
        while j >= 0 and curr < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = curr


my_list = [38, 27, 43, 3, 9, 82, 10]
insertion_sort(my_list)
print(my_list)
