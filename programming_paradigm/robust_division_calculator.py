# robust_division_calculator.py
def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Perform division
        result = numerator / denominator
        return f"The result of dividing {numerator} by {denominator} is: {result}"
    
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    
    except ValueError:
        return "Error: Non-numeric input provided. Please provide valid numbers."

