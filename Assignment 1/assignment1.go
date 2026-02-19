package main

import (
	"fmt"
	"math/rand"
	"time"
)

func insertionSort(arr []int) {
	for j := 1; j < len(arr); j++ {
		key := arr[j]
		i := j - 1
		for i >= 0 && arr[i] > key {
			arr[i+1] = arr[i]
			i--
		}
		arr[i+1] = key
	}
}

func main() {
	sizes := []int{1000, 5000, 10000, 20000}

	for _, n := range sizes {
		arr := make([]int, n)
		for i := range arr {
			arr[i] = rand.Intn(100000)
		}

		start := time.Now()
		insertionSort(arr)
		elapsed := time.Since(start)
		fmt.Printf("Go: Insertion Sort n=%d, time=%s\n", n, elapsed)
	}
}
