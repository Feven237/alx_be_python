#!/usr/bin/python3

# Get user input
number = int(input("Enter a number to generate its multiplication table: "))

# Generate the multiplication table
for i in range(1, 11):  # Correct range for 1 to 10
    result = number * i
    print(f"{number} x {i} = {result}")
