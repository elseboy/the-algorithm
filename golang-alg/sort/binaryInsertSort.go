package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {

	list := []int{1, 67, 33, 20, 5, 6, 71, 8}
	fmt.Println(binaryInsertSort(list))

}

// ===
// 二分插入快速排序 （每次能砍掉一半循环）
// ===
func binaryInsertSort(arr []int) []int {
	for i := 1; i < len(arr); i++ {
		// 循环插入寻找中间索引位置
		index := findMiddleIndex(arr, 0, i-1, i)
		fmt.Println("索引是=====>", index)
		if index != i {
			temp := arr[i]
			for j := i; j > index; j-- {
				// 交换移动
				arr[j], arr[j-1] = arr[j-1], arr[j]
			}
			arr[index] = temp
		}
	}
	return arr
}

// 寻找中间的索引
func findMiddleIndex(arr []int, start int, end int, current int) int {
	// 1, 67, 33, 20, 5, 6, 71, 8
	// 对比当前位置与需要排序的元素大小 返回较大值的位置
	if start >= end {
		if arr[start] < arr[current] {
			return current
		} else {
			return start
		}
	}
	middle := (start + end) / 2
	if arr[middle] > arr[current] {
		return findMiddleIndex(arr, start, end, current)
	} else {
		return findMiddleIndex(arr, middle+1, end, current)
	}
}

func makeRandomArray() []int {
	var length = 100
	var list []int
	randNum := rand.New(rand.NewSource(time.Now().UnixNano()))
	for i := 0; i < length; i++ {
		list = append(list, int(randNum.Intn(1000)))
	}
	fmt.Println(list)
	return list
}
