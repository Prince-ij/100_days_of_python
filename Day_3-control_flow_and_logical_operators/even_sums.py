#!/bin/env python3

print("This sums all even numbers between 1 and 100 inclusive")

even_sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        even_sum += i

print(even_sum)
