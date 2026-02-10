# Name: Sean Nguyen
# Date: 2026-02-10
# Purpose: Contacts module for a Tuffy Titan Contact List (add/modify/delete/print/combine).

def print_list(contacts):
    """Print the contact list with index, first name, and last name."""
    print("\n================== CONTACT LIST ==================")
    print("Index   First Name            Last Name")
    print("======  ====================  ====================")
    for i in range(len(contacts)):
        print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')


def add_contact(contacts):
    """Prompt for a first and last name, then add the contact to the list."""
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    contacts.append([first, last])
    return contacts


def modify_contact(contacts):
    """Modify an existing contact at the provided index."""
    idx_str = input("Enter the index number: ")
    try:
        idx = int(idx_str)
    except ValueError:
        print("Invalid index number.")
        return contacts

    if idx < 0 or idx >= len(contacts):
        print("Invalid index number.")
        return contacts

    first = input("Enter first name: ")
    last = input("Enter last name: ")
    contacts[idx] = [first, last]
    return contacts


def delete_contact(contacts):
    """Delete an existing contact at the provided index."""
    idx_str = input("Enter the index number: ")
    try:
        idx = int(idx_str)
    except ValueError:
        print("Invalid index number.")
        return contacts

    if idx < 0 or idx >= len(contacts):
        print("Invalid index number.")
        return contacts

    del contacts[idx]
    return contacts


def combine_contact(contacts, new_contacts):
    """Combine two contact lists into one list."""
    contacts.extend(new_contacts)
    return contacts
