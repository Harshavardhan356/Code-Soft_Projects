print(" Contact Book Application \n")

contacts = []


def add_contact():
    print("\n Add New Contact ")
    name = input("Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully.\n")


def view_contacts():
    print("\n-- All Contacts --")
    if not contacts:
        print("No contacts found.\n")
        return

    for idx, c in enumerate(contacts, 1):
        print(f"{idx}. {c['name']} - {c['phone']}")
    print()


def search_contact():
    print("\n-- Search Contact --")
    keyword = input("Enter name or phone to search: ")

    found = False
    for c in contacts:
        if keyword.lower() in c['name'].lower() or keyword in c['phone']:
            print("\nContact Found:")
            print("Name:", c['name'])
            print("Phone:", c['phone'])
            print("Email:", c['email'])
            print("Address:", c['address'])
            found = True
            break

    if not found:
        print("No matching contact found.\n")


def update_contact():
    print("\n-- Update Contact --")
    name_to_update = input("Enter the name of the contact to update: ")
    for c in contacts:
        if c['name'].lower() == name_to_update.lower():
            print("Contact found. Leave blank to keep existing value.")

            new_name = input("New Name (current: " + c['name'] + "): ") or c['name']
            new_phone = input("New Phone (current: " + c['phone'] + "): ") or c['phone']
            new_email = input("New Email (current: " + c['email'] + "): ") or c['email']
            new_address = input("New Address (current: " + c['address'] + "): ") or c['address']

            c['name'] = new_name
            c['phone'] = new_phone
            c['email'] = new_email
            c['address'] = new_address

            print("Contact updated successfully.\n")
            return
    print("Contact not found.\n")


def delete_contact():
    print("\n-- Delete Contact --")
    name_to_delete = input("Enter the name of the contact to delete: ")

    for c in contacts:
        if c['name'].lower() == name_to_delete.lower():
            contacts.remove(c)
            print("Contact deleted successfully.\n")
            return
    print("Contact not found.\n")


def main_menu():
    while True:
        print("==== Contact Book Menu ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")


main_menu()
