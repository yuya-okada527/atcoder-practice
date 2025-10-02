package main

import (
	"fmt"
)

func main() {
	var x string
	fmt.Scan(&x)
	var result = "";
	for i := 0; i < len(x); i++ {
		if !isVowels(x[i]) {
			result += string(x[i])
		}
	}
	fmt.Println(result)
}

func isVowels(x byte) bool {
	switch x {
	case 'a', 'i', 'u', 'e', 'o':
		return true
	default:
		return false
	}
}
