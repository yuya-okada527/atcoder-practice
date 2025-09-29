package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	if n % 3 == 0 {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
