# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations based on the operation parameter.
    
    Parameters:
    num1 (float): The first number
    num2 (float): The second number
    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
    float or str: The result of the arithmetic operation or an error message for division by zero
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operation"

# Example usage
if __name__ == "__main__":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ")
    result = perform_operation(num1, num2, operation)
    print(f"The result is: {result}")


