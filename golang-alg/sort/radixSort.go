package main

import (
	"fmt"
)

func main() {

	arr := []int{1, 9, 10, 30, 2, 5, 45, 8, 63, 234, 2, 12, 87, 66}
	fmt.Println(radixSort(arr))
}

func radixSort(arr []int) []int {
	max := getMaxNum(arr)
	for bit := 1; max/bit > 0; bit *= 10 {
		// 按照数量级分段
		fmt.Println("before", arr)
		// 每次处理一个级别的排序 （个位数 十位数 百位数...）
		bitSort(arr, bit)
		fmt.Println("after", arr)
	}
	return arr
}

func bitSort(arr []int, bit int) []int {
	// 数组长度
	length := len(arr)
	// 统计长度
	bitCounts := make([]int, 20)
	for i := 0; i < length; i++ {
		// 取模
		num := (arr[i] / bit) % 10
		// 统计余数相等个数
		bitCounts[num]++
	}
	fmt.Println(bitCounts)
	for i := 1; i < 20; i++ {
		// 实现叠加 计算位置
		bitCounts[i] += bitCounts[i-1]
	}
	fmt.Println(bitCounts)
	temp := make([]int, 20)
	for i := length - 1; i >= 0; i-- {
		num := (arr[i] / bit) % 10
		temp[bitCounts[num]-1] = arr[i]
		bitCounts[num]--
	}
	// 保存数组
	for i := 0; i < length; i++ {
		arr[i] = temp[i]
	}
	return arr

}

func getMaxNum(a []int) int {
	max := a[0]
	for i := 1; i < len(a); i++ {
		if a[i] > max {
			max = a[i]
		}
	}
	return max
}
