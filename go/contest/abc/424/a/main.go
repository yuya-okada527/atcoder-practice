package main

import (
	"fmt"
)

func main() {
	var a, b, c int
	fmt.Scan(&a, &b, &c)
	allPositive := a > 0 && b > 0 && c > 0
	isTriangle := a + b > c && b + c > a && c + a > b
	isIsosceles := a == b || b == c || c == a
	if allPositive && isTriangle && isIsosceles {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
