# Step 1: Get the size from the user
size = int(input("Enter the size of the pattern: "))

# Step 2: Initialize the row counter to 1
row = 1

# Step 3: While loop to iterate through each row
while row <= size:  # Continue the loop until the row counter reaches the size
    # Step 4: Nested for loop to print the asterisks for each row
    for _ in range(size):  # Prints 'size' number of asterisks in a row
        print("*", end="")  # Keeps the asterisks on the same line
    
    print()  # Move to the next line after printing a row
    row += 1  # Increment the row counter to go to the next row
