# main.py

from arithmetic_operations import perform_operation

# Example numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Operation input
operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()

# Perform the operation
result = perform_operation(num1, num2, operation)

# Display the result
print("Result:", result)

