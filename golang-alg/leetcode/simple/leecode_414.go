package main

import (
	"fmt"
)

func main() {
	arr := []int{2, 2, 3, 1, 4}
	fmt.Println(thirdMax(arr))
}

/**
func thirdMax(arr []int) int {
    if len(arr) == 2 {
        return getMax(arr[0], arr[1])
    }
    var mapInt = make(map[int]int)
    for i := 0; i <= len(arr)-1; i++ {
        mapInt[arr[i]] = arr[i]
    }
    var newArr = []int{}
    for k, _ := range mapInt {
        newArr = append(newArr, k)
    }
    for i := 0; i <= len(newArr)-1; i++ {
        for j := i + 1; j < len(newArr); j++ {
            if newArr[i] < newArr[j] {
                newArr[i], newArr[j] = newArr[j], newArr[i]
            }
        }
    }
    return newArr[2]
}

func getMax(i int, j int) int {
    if i > j {
        return i
    } else {
        return j
    }
}
*/

func thirdMax(arr []int) int {
	a, b, c := -1<<31, -1<<31, -1<<31
	m := make(map[int]bool)
	for i := 0; i < len(arr); i++ {
		m[arr[i]] = true
		if arr[i] > a {
			a, b, c = arr[i], a, b
			fmt.Println("aaa", a, b, c)
		} else if arr[i] < a && arr[i] > b {
			b, c = arr[i], b
			fmt.Println("bbb", b)
		} else if arr[i] < b && arr[i] > c {
			c = arr[i]
			fmt.Println("ccc", c)
		}
	}
	if len(m) < 3 {
		return a
	}
	return c
}
