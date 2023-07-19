package main

import (
	"fmt"
)

func main() {
	list := []string{"123", "123", "342", "3444", "343", "343", "768", "999", "999", "343"}
	dupByList(list)
	dupByMap(list)
	arr := []int{2, 3, 1, 0, 2, 5, 3, 34, 34, 67, 38, 3, 0, 3, 2, 67}
	dupAndCountAndSort(arr)
}

// 双层循环
func dupByList(arr []string) []string {
	if len(arr) <= 0 {
		return arr
	}
	var result []string
	for i := range arr {
		flag := true
		for j := range result {
			if arr[i] == result[j] {
				flag = false
				break
			}
		}
		if flag {
			result = append(result, arr[i])
		}
	}
	fmt.Println(result)
	return result
}

// map去重并计算出现次数
func dupByMap(arr []string) []string {
	if len(arr) <= 0 {
		return arr
	}
	var result []string
	newMap := make(map[string]int)
	for _, s := range arr {
		if 0 == newMap[s] {
			newMap[s] = 1
		} else {
			newMap[s] = newMap[s] + 1
		}
	}
	for k, v := range newMap {
		result = append(result, k)
		fmt.Println("element: ", k, " times: ", v)
	}
	fmt.Println(result)
	return result
}

// 去重统计排序
func dupAndCountAndSort(arr []int) []int {
	if len(arr) <= 0 {
		return arr
	}
	fmt.Println("the original array is ", arr)
	var afterDup []int
	dupMap := make(map[int]int)
	for _, e := range arr {
		if dupMap[e] == 0 {
			dupMap[e] = 1
		} else {
			dupMap[e] = dupMap[e] + 1
		}
	}
	for k, v := range dupMap {
		afterDup = append(afterDup, k)
		fmt.Println("element: ", k, " count: ", v)
	}
	fmt.Println("after dup ", afterDup)
	result := quickSortArr(afterDup)
	fmt.Println("after sort ", result)
	return result
}

func quickSortArr(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}
	split := arr[0]
	var low []int
	var high []int
	var middle []int
	middle = append(middle, split)
	for i := 1; i < len(arr); i++ {
		e := arr[i]
		if e < split {
			low = append(low, e)
		} else if e > split {
			high = append(high, e)
		} else {
			middle = append(middle, e)
		}
	}
	low, high = quickSortArr(low), quickSortArr(high)
	result := append(append(low, middle...), high...)
	return result
}
