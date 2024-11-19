#!/bin/python3

def print_calc(height, width, cover):
    res = height * width / cover
    print(round(res))

test_h = int(input("Enter height of wall: "))
test_w = int(input("Enter width of wall: "))
coverage = 5

print_calc(width=test_w, height=test_h, cover=coverage)
