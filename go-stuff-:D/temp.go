package main

import (
	"fmt"
	"runtime"
)

func main() {
	var count = runtime.NumCPU()
	fmt.Println(count)
}
