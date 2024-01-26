import re

contacts = []

def is_valid_mobile_number(number):
    return re.match(r'^\d{10}$', number) is not None

def add_contact():
    name = input("Enter name: ")
    while True:
        phone = input("Enter the phone number: ")
        if is_valid_mobile_number(phone):
            break
        else:
            print("Invalid phone number. Please enter a 10-digit number.")
    contact = {"name": name, "phone": phone}
    contacts.append(contact)
    print("Added Successfully...")

def delete_contact():
    name = input("Enter name:")
    for contact in contacts[:]:
        if contact["name"] == name:
            contacts.remove(contact)
            print("Delete Successfully...")
            return
    print("Contact not found.")

def edit_contact():
    name = input("Enter the name you want to edit: ")
    change = input("Enter what you want to change (name or number): ")
    for contact in contacts:
        if contact["name"] == name:
            if change == "name":
                contact["name"] = input("Enter the new name: ")
                print("Edited name Successfully... ")
            elif change == "number":
                while True:
                    new_number = input("Enter the new number: ")
                    if is_valid_mobile_number(new_number):
                        contact["phone"] = new_number
                        print("Edited number Successfully... ")
                        break
                    else:
                        print("Invalid phone number. Please enter a 10-digit number.")
            else:
                print("Choose the correct option!")
            return
    print("Contact not found.")

def search_contact():
    name_pattern = input("Enter the name you want to search: ")
    for contact in contacts:
        if re.search(name_pattern, contact["name"], re.IGNORECASE):
            print(f"Name: {contact['name']} and Phone No.: {contact['phone']}")

def search_by_mobilenumber():
    search_pattern = input("Enter the name or mobile number you want to search: ")
    for contact in contacts:
        if re.search(search_pattern, contact["name"], re.IGNORECASE) or re.search(search_pattern, contact["phone"]):
            print(f"Name: {contact['name']} and Phone No.: {contact['phone']}")

def display_contact():
    print("All the contact list:")
    print("     Name                Phone Number ")
    print("----------------------------------------")
    for contact in contacts:
        print(f"    {contact['name']}               {contact['phone']}")

def contactbook():
    print("***** Welcome to Contact Book! *****\n")
    print("## List of functionality ##\n 1. Add\n 2. Delete\n 3. Edit\n 4. Search\n 5. Search by mobilenumber\n 6. Display\n ")
    user_choice = input("Enter your Choice: ")
    if user_choice == "1":
        add_contact()
    elif user_choice == "2":
        delete_contact()
    elif user_choice == "3":
        edit_contact()
    elif user_choice == "4":
        search_contact()
    elif user_choice == "5":
        search_by_mobilenumber()
    elif user_choice == "6":
        display_contact()
    user = input("Do you Want to Continue? (y/n): ")
    if user.lower() == "y":
        contactbook()

contactbook()
