#!/bin/env python3
print("Average height Computer ")

heights = input("Enter the list of heights seperated by space : ").split()

for i in range(0, len(heights)):
    heights[i] = int(heights[i])

total_height = 0
for height in heights:
    total_height += height

num_height = 0
for i in heights:
    num_height += 1

average = total_height / num_height

print("Average of heights is", average)
