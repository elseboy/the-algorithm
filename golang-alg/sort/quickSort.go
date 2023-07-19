package main

import (
	"fmt"
	"time"
)

func main() {
	arr := []int{1, 9, 10, 30, 2, 5, 45, 8, 63, 234, 12, 87, 66}
	t1 := time.Now()
	fmt.Println(quickSort(arr))
	fmt.Println(time.Now().Sub(t1).Microseconds())
}

// ===
// 快排
// ===
func quickSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}
	// 以数组第一个元素为基准
	base := arr[0]
	// 存储比base小的
	var left []int
	// 存储比base大的
	var right []int
	// 存储跟base相等的
	var middle []int
	// 加入base首先
	middle = append(middle, base)

	for i := 1; i < len(arr); i++ {
		if arr[i] < base {
			left = append(left, arr[i])
		} else if arr[i] > base {
			right = append(right, arr[i])
		} else {
			middle = append(middle, arr[i])
		}
	}
	// 切割递归处理
	left, right = quickSort(left), quickSort(right)
	newArr := append(append(left, middle...), right...)
	fmt.Println(newArr)
	return newArr
}
