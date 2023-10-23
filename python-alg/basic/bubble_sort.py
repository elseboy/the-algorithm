def bubble_sort(array):
    swapped = False
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break


my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print(my_list)
