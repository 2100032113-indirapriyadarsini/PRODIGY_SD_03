import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts(contacts):
    if contacts:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']}, {contact['phone']}, {contact['email']}")
    else:
        print("No contacts available.")

def edit_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the number of the contact to edit: ")) - 1
    if 0 <= index < len(contacts):
        contacts[index]['name'] = input("Enter new name: ")
        contacts[index]['phone'] = input("Enter new phone number: ")
        contacts[index]['email'] = input("Enter new email address: ")
        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Invalid contact number.")

def delete_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the number of the contact to delete: ")) - 1
    if 0 <= index < len(contacts):
        contacts.pop(index)
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Invalid contact number.")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
