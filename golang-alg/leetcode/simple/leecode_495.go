package main

import "fmt"

func main() {
	fmt.Println(findPoisonedDuration([]int{1, 2}, 2))
}

func findPoisonedDuration(timeSeries []int, duration int) int {
	if len(timeSeries) == 0 {
		return 0
	}
	if len(timeSeries) == 1 {
		return duration
	}
	total := 0
	for i := 0; i < len(timeSeries)-1; i++ {
		if timeSeries[i+1]-timeSeries[i] >= duration {
			total += duration
		} else {
			total = timeSeries[i+1] - timeSeries[i] + total
		}
	}
	return total + duration
}
