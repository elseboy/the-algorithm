package main

import "fmt"

func main() {
	arr := []int{1}
	fmt.Println(findMaxConsecutiveOnes(arr))
}

//===
//给定一个二进制数组， 计算其中最大连续1的个数。
//===
func findMaxConsecutiveOnes(arr []int) int {
	var count int
	var temp int
	for i := 0; i <= len(arr)-1; i++ {
		if arr[i] == 1 {
			temp++
		} else {
			temp = 0
		}
		if temp > count {
			count = temp
		}
	}
	return count
}
