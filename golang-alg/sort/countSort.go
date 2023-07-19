package main

import (
	"fmt"
)

func main() {

	arr := []int{1, 9, 10, 30, 2, 5, 45, 8, 63, 234, 2, 12, 87, 66}
	fmt.Println(countSort(arr))
}
func countSort(arr []int) []int {
	n := len(arr)
	if n <= 1 {
		return arr
	}
	var max int
	for i := range arr {
		if arr[i] > max {
			max = arr[i]
		}
	}
	c := make([]int, max+1)
	for i := range arr {
		c[arr[i]]++
	}
	for i := 1; i <= max; i++ {
		c[i] += c[i-1]
	}

	r := make([]int, n)
	for i := n - 1; i >= 0; i-- {
		index := c[arr[i]] - 1
		r[index] = arr[i]
		c[arr[i]]--
	}
	copy(arr, r)
	return arr
}
