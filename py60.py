contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added.")

    elif choice == 2:
        name = input("Enter name to search: ")
        print("Phone:", contacts.get(name, "Not found"))

    elif choice == 3:
        name = input("Enter name to update: ")
        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone
            print("Updated successfully.")
        else:
            print("Contact not found.")

    elif choice == 4:
        name = input("Enter name to delete: ")
        contacts.pop(name, None)
        print("Deleted successfully.")

    elif choice == 5:
        break