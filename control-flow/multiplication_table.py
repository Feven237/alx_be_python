number = int(input("Enter a number to see its multiplication table: "))  # Ask for user input

# Generate and print the multiplication table
for Y in range(1, 11):  # Loop from 1 to 10
    X = number  # X is the user's number
    Z = X * Y  # Z is the product
    print(f"{X} * {Y} = {Z}")  # Print in the format: X * Y = Z

