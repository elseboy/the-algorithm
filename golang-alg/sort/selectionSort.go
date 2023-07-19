package main

import (
	"fmt"
)

func main() {
	arr := []int{1, 9, 2, 10, 30, 5, 45, 8}
	fmt.Println(selectionSort(arr))
}

// ===
// 选择排序
// ===
func selectionSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}
	for i := 0; i < len(arr)-1; i++ {
		minIndex := i
		for j := i + 1; j < len(arr); j++ {
			if arr[j] < arr[minIndex] {
				minIndex = j
			}
		}
		arr[i], arr[minIndex] = arr[minIndex], arr[i]
	}
	return arr
}
