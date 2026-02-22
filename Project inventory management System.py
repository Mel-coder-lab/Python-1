# Inventory
inventory = []
# Add a new item

def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))
    category = input("Enter category: ")
    # item in dictionary
    new_item = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    }
    inventory.append(new_item)
    print("Item Added!")

def view_inventory():
    print("\n--- Current Inventory ---")
    if not inventory:
        print("Inventory is empty.")
    for item in inventory:
        print(f"Name: {item['name']} | Price: {item['price']} | Qty: {item['quantity']} | Cat: {item['category']}")

def update_item():
    target = input("Which item do you want to update? ")
    for item in inventory:
        if item["name"] == target:

            new_price = float(input("Enter new price: "))

            item["price"] = new_price
            print("Price Updated!")
            return      #item found , we can stop looking!
    print("Item not found.")

def delete_item():
    target = input("Which item do you want to delete? ")
    for item in inventory:
        if item["name"] == target:
            inventory.remove(item)
            print("Item Deleted!")
            return
        print("Item not found.")

def search_by_category():
    # Step 1: get the users search term
    query = input("What category do you want to search for? : ")
    found = False
    for item in inventory:
        if item["category"] == query:
            print(f"- {item['name']} ( ${item['price']}")
            found = True

    if not found :
        print("Item not found in that category.")
# creating the menu and wrapping up
while True:
    print("\n--- Market Management System ---")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Item")
    print("4. Remove Item")
    print("5. Search by Category")
    print("6. Exit")
    choice = input("Select an option (1-6): ")
    if choice == "1":
        add_item()
    elif choice == "2":
        view_inventory()
    elif choice == "3":
        update_item()
    elif choice == "4":
        delete_item()
    elif choice == "5":
        search_by_category()
    elif choice == "6":
        print("Thank you for using this program!")
        break
    else:
         print("invalid input, please try again.")

