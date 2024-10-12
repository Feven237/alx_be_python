# robust_division_calculator.py
def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Perform division
        result = numerator / denominator
        return f"The result of the division is {result}"  # Adjusted output format
        
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Non-numeric input provided. Please provide valid numbers."


