package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	result := float64(0)
	for i := 1; i <= n; i++ {
		result += float64(10000*i) / float64(n)
	}
	fmt.Println(result)
}
