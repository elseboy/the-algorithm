package main

import (
	"fmt"
)

func main() {

	arr := []int{1, 9, 10, 30, 2, 5, 45, 8, 63, 234, 2, 12, 87, 66}
	fmt.Println(mergeSort(arr))
}

//===
//归并排序
//===
func mergeSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}
	length := len(arr)
	middle := length / 2
	leftArr := mergeSort(arr[:middle])
	rightArr := mergeSort(arr[middle:])
	return merge(leftArr, rightArr)
}

func merge(leftArr []int, rightArr []int) []int {
	leftIndex := 0
	rightIndex := 0
	var newArr []int
	for leftIndex < len(leftArr) && rightIndex < len(rightArr) {
		if leftArr[leftIndex] < rightArr[rightIndex] {
			newArr = append(newArr, leftArr[leftIndex])
			leftIndex++
		} else if leftArr[leftIndex] > rightArr[rightIndex] {
			newArr = append(newArr, rightArr[rightIndex])
			rightIndex++
		} else {
			newArr = append(newArr, leftArr[leftIndex])
			newArr = append(newArr, rightArr[rightIndex])
			leftIndex++
			rightIndex++
		}
	}
	for leftIndex < len(leftArr) {
		newArr = append(newArr, leftArr[leftIndex])
		leftIndex++
	}
	for rightIndex < len(rightArr) {
		newArr = append(newArr, rightArr[rightIndex])
		rightIndex++
	}
	return newArr
}
