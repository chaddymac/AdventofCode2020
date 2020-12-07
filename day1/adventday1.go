package main

import (
	"bufio"
	"fmt"
	_ "math"
	"os"
	"strconv"
)

func main() {
	partOne()
	partTwo()
}

func ReturnList() []int {
	var x []int
	// Open the file.
	f, _ := os.Open("adventday1numbers.txt")
	// Create a new Scanner for the file.
	scanner := bufio.NewScanner(f)
	// Loop over all lines in the file and print them.

	for scanner.Scan() {
		line := scanner.Text()
		num, _ := strconv.Atoi(line)
		x = append(x, num)

	}
	return x
}

//loop over numbers to multiply them by themselves
func partOne() int {
	x := ReturnList()
	year := 2020
	ans1 := 0
out:
	for _, v := range x {
		for _, v2 := range x {
			add1 := v + v2
			if add1 == year {
				ans1 := v * v2
				fmt.Println(ans1)
				break out
			}
		}

	}
	return ans1
}

func partTwo() int {
	x := ReturnList()
	year := 2020
	ans2 := 0
out:
	for _, v := range x {
		for _, v2 := range x {
			for _, v3 := range x {
				add2 := v + v2 + v3
				if add2 == year {
					ans2 := v * v2 * v3
					fmt.Println(ans2)
					break out
				}
			}

		}
	}
	return ans2
}
