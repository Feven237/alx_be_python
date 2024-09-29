def display_menu():
    print ("Shopping Manager List")
    print ("1 Add item")
    print ("2 Remove item")
    print ("3 Vist List")
    print ("4 Exit")
def main():
    Shopping_List = []
    while True :
        display_menu()
        choice = input( "Enter your choice: " )
        if choice == '1':
            # Prompt for and add an item
            pass
        elif choice == '2':
            # Prompt for and remove an item
            pass
        elif choice == '3':
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()