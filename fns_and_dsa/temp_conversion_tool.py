# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Factor for converting Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Factor for converting Celsius to Fahrenheit
FAHRENHEIT_OFFSET = 32  # Offset for converting Fahrenheit to Celsius

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

def main():
    # Prompt the user for temperature input
    temp_input = input("Enter the temperature to convert: ")
    
    try:
        # Convert input to float for temperature
        temperature = float(temp_input)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    # Ask the user for the temperature scale
    scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if scale == 'C':
        # Convert Celsius to Fahrenheit
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    elif scale == 'F':
        # Convert Fahrenheit to Celsius
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    else:
        print("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
