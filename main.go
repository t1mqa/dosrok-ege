package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
)

func main() {
    // Read input file
    file, err := os.Open("27task.txt")
    if err != nil {
        panic(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)

    // Read minimum time between measurements
    scanner.Scan()
    k, err := strconv.Atoi(scanner.Text())
    if err != nil {
        panic(err)
    }

    // Read measurements
    var measurements []int
    for scanner.Scan() {
        m, err := strconv.Atoi(scanner.Text())
        if err != nil {
            panic(err)
        }
        measurements = append(measurements, m)
    }

    // Find maximum sum of two measurements
    var maxSum int
    for i := 0; i < len(measurements); i++ {
        for j := i + 1; j < len(measurements); j++ {
            if j-i >= k {
                sum := measurements[i] + measurements[j]
                if sum > maxSum {
                    maxSum = sum
                }
            }
        }
    }

    fmt.Println(maxSum)
}