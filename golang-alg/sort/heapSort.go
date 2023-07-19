package main

import "fmt"

func main() {
	arr := []int{6, 0, 1, 3, 17, 2, 28, 3}
	fmt.Println(HeapSort(arr))
}

//===
// 堆排序
// 1：构建大顶堆（最浪费时间的时候）
// 2：调整大顶堆（）
//===

func HeapSort(nums []int) []int {
	if len(nums) <= 1 {
		return nums
	}

	N := len(nums) - 1
	//从底部到顶部构建大顶堆，最后一个非叶子节点开始
	for i := N / 2; i >= 0; i-- {
		sink(nums, i, N)
	}

	//将堆顶值和末尾交换，重新调整堆
	for i := N; i >= 0; i-- {
		swap(nums, 0, i)
		sink(nums, 0, i-1) //交换之后，数组最后一位不算在堆内，需要减1操作
	}

	//不同写法，结果一样
	/*for N>=0{
	    wap(nums,0,N)
	    N--
	    sink(nums,0,N)
	}*/
	return nums
}

func sink(nums []int, k, N int) {
	for {
		i := 2*k + 1
		if i > N {
			break
		}
		//找左右子节点最大值
		if i+1 <= N && nums[i+1] > nums[i] {
			i++
		}
		//已经大于最大值，不需要再交换
		if nums[k] >= nums[i] {
			break
		}
		swap(nums, k, i)
		k = i //继续向上调整
	}
	fmt.Println(nums, k, N)
}

func swap(nums []int, x, y int) {
	nums[x], nums[y] = nums[y], nums[x]
}
