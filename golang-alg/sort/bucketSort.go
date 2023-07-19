package main

import (
	"fmt"
)

func main() {

	arr := []int{1, 9, 10, 30, 2, 5, 45, 8, 63, 234, 2, 12, 87, 66}
	fmt.Println(bucketSort(arr))
}

func bucketSort(arr []int) []int {
	if len(arr) < 1 {
		return arr
	}
	array := make([]int, getMax(arr)+1)
	for i := 0; i < len(arr); i++ {
		array[arr[i]]++
	}
	c := make([]int, 0)
	for i := 0; i < len(array); i++ {
		for array[i] != 0 {
			c = append(c, i)
			array[i]--
		}
	}
	copy(arr, c)
	return arr
}

// 获取待排序数组中的最大值
func getMax(a []int) int {
	max := a[0]
	for i := 1; i < len(a); i++ {
		if a[i] > max {
			max = a[i]
		}
	}
	return max
}
