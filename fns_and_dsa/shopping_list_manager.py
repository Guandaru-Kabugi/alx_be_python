def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Please add an item to the shopping list: ")
            shopping_list.append(item)
            print(f"{item} added successfully.")
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to add: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed successfully.")
            elif not item in shopping_list:
                print("Item not found")
        elif choice == '3':
            # Display the shopping list
            print("Here is your list of items: ")
            for item in shopping_list:
                print(item)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()