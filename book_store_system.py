#Book store inventory system:
inventory={}

#starting design:
print("\n\t\t\t\t\t*********************************************"
      "\n\t\t\t\t\t^^^^^^^^ Book Store inventory System^^^^^^^^^"
      "\n\t\t\t\t\t*********************************************")

#functions:

#Here we are adding the book in inventory:
def add():
    add_data = int(input("\nHow many Books  do you want to add?  "))

    for i in range(add_data):
        book_title = input(f"Enter book's title {(i+1)}: ")
        book_quantity = int(input("Enter its quantity: "))
        inventory[book_title] = book_quantity

    print("  Books  are added successfully in inventory.")
    for title, quantity in inventory.items():
        print(f"{title}: {quantity}")



#Here we are removing books from inventory:
def remove():
    remove_books=input("\nEnter Book's title that removed from inventory: ")
    if remove_books in inventory:
        del inventory[remove_books]
        print(f"{remove_books} removed successfully from inventory.\nReamining Books are:")
        for title, quantity in inventory.items():
            print(f"{title}: {quantity}")
    else:
        print(f"{remove_books} is not found in inventory")



# Here Display present inventory:
def view():
    print("\nCurrent inventory")
    for title, quantity in inventory.items():
        print(f"{title}: {quantity}")


#Here Sum and display the total books:
def total_books():
    print("Inventory:", inventory)  #Here we  print the inventory to check its contents
    total = sum(inventory.values())
    print(f"Total book's quantity in inventory: {total}")



#Here exist the program:
def end():
    print("Experience the power of organized inventory management System!")


#main part of program:
while True:
    print("\nBookstore Inventory Management System"
          "\n1. Add book"
          "\n2. Remove book"
          "\n3. Display inventory"
          "\n4. Total books"
          "\n5. Exit")
    action=input("Decide your action: ")

    if action == "1":
        add()
    elif action == "2":
        remove()
    elif action == "3":
        view()
    elif action == "4":
        total_books()
    elif action == "5":
        end()
        break
    else:
        print("Invalid action. Please try again.\nAnd select correct option from the given options  ")






