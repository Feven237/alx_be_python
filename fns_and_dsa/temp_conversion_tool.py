
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    celsius = (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
     fahrenheit = (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32
    return fahrenheit
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
