# from contacts import * # Importing all functions from contacts module

# Name: Sean Nguyen
# Date: 2026-02-10
# Purpose: Driver program for the Tuffy Titan Contact List.

import contacts

def main():
    contact_list = []

    while True:
        print("\n      *** TUFFY TITAN CONTACT MAIN MENU\n")
        print("1. Print list")
        print("2. Add contact")
        print("3. Modify contact")
        print("4. Delete contact")
        print("5. Exit the program\n")

        choice = input("Enter menu choice: ")

        if choice == "1":
            contacts.print_list(contact_list)

        elif choice == "2":
            contact_list = contacts.add_contact(contact_list)

        elif choice == "3":
            contact_list = contacts.modify_contact(contact_list)

        elif choice == "4":
            contact_list = contacts.delete_contact(contact_list)

        elif choice == "5":
            break

        else:
            # Invalid menu choice (not specified in output, so do nothing)
            pass


if __name__ == "__main__":
    main()
