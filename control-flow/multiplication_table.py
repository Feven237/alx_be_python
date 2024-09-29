number = int(input("Enter a number to see its multiplication table: "))  # Ask for user input

# Generate and print the multiplication table
for i in range(1, 11):  # Loop from 1 to 10
    z = number * i  # Calculate the product
    print(f"{number} * {i} = {z}")  # Print in the format: number * i = z



