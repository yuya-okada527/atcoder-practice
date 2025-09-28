package main

import (
	"fmt"
	"math"
)

func main() {
	var n int
	fmt.Scan(&n)
	var x float64
	for i := 1; i <= n; i++ {
		x += math.Pow(-1, float64(i)) * math.Pow(float64(i), 3)
	}
	fmt.Println(x)
}

