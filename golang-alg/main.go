package main

import (
	"fmt"
	"time"
)

func isValid(grid [][]int, row, col, num int) bool {
	// Check if the number already exists in the row
	for _, val := range grid[row] {
		if val == num {
			return false
		}
	}

	// Check if the number already exists in the column
	for r := 0; r < 9; r++ {
		if grid[r][col] == num {
			return false
		}
	}

	// Check if the number already exists in the 3x3 box
	boxRow := (row / 3) * 3
	boxCol := (col / 3) * 3
	for r := boxRow; r < boxRow+3; r++ {
		for c := boxCol; c < boxCol+3; c++ {
			if grid[r][c] == num {
				return false
			}
		}
	}

	return true
}

func solveSudoku(grid [][]int) bool {
	for row := 0; row < 9; row++ {
		for col := 0; col < 9; col++ {
			if grid[row][col] == 0 {
				for num := 1; num <= 9; num++ {
					if isValid(grid, row, col, num) {
						grid[row][col] = num
						printSudoku(grid)                  // Print the current state of the grid
						time.Sleep(100 * time.Millisecond) // Introduce a delay of 100 milliseconds
						if solveSudoku(grid) {
							return true
						}
						grid[row][col] = 0
					}
				}
				return false
			}
		}
	}
	return true
}

func printSudoku(grid [][]int) {
	for _, row := range grid {
		for _, num := range row {
			fmt.Printf("%d ", num)
		}
		fmt.Println()
	}
	fmt.Println("-------------------")
}

func guessSudoku(target [][]int) {
	solveSudoku(target)
	fmt.Println("Target Sudoku found!")
	printSudoku(target)
}

func main() {
	targetSudoku := [][]int{
		{0, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 0},
	}
	startTime := time.Now()

	guessSudoku(targetSudoku)
	elapsedTime := time.Since(startTime)
	fmt.Printf("Sudoku solved in %s\n", elapsedTime)
}
