package main

import (
	"fmt"
)

func main() {
	arr := []int{6, 0, 1, 3, 17, 2, -1, 3}
	fmt.Println(bubbleSort(arr))
}

// ===
// 冒泡排序
// ===
func bubbleSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}

	for i := 0; i < len(arr)-1; i++ {
		for j := i + 1; j < len(arr); j++ {
			if arr[i] < arr[j] {
				arr[i], arr[j] = arr[j], arr[i]
			}
		}
	}
	return arr
}
