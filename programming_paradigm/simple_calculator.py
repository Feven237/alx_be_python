class SimpleCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):  # Fixed the typo here
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"  # Handle division by zero gracefully
