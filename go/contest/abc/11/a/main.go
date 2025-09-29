package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	if n == 12 {
		fmt.Println(1)
	} else {
		fmt.Println(n+1)
	}
}
