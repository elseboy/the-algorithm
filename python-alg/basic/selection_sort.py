def selection_sort(arr):
    for i in range(len(arr)):
        smallest_index = i
        for j in range(smallest_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        if smallest_index != i:
            temp = arr[i]
            arr[i] = arr[smallest_index]
            arr[smallest_index] = temp


my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(my_list)
print(my_list)
