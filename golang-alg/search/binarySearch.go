package main

import (
	"fmt"
)

func main() {
	arr := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	fmt.Println(binarySearch(arr, 3))
}

// ===
// 前提是排好序的array
// ===
func binarySearch(arr []int, n int) int {
	if len(arr) <= 1 {
		return 0
	}
	left := 0
	right := len(arr) - 1
	for left <= right {
		middle := (left + right) / 2
		if arr[middle] > n {
			right = middle - 1
			fmt.Println("right", right)
		} else if arr[middle] < n {
			left = middle + 1
			fmt.Println("left", left)
		} else {
			fmt.Println("middle", middle)
			return middle
		}
	}
	return -1
}
