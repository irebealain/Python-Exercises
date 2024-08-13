# A new dictionary to hold all contacts.
contacts = {}


# A function that helps to add new contacts in the dictionary.
def add_contact(names, phone_number):
    contacts[names] = phone_number


# A function that helps to delete a contacts in the dictionary.
def delete_contact(names):
    if names in contacts:
        del contacts[names]
        print("Your account has been deleted")
    elif names not in contacts:
        print("Your account does not exist")


# A function that helps to search a contact from the dictionary.
def search_contact(names):
    if names in contacts:
        print(f"Your account {names} has been found")
    else:
        print("Your account does not exist")


# Questions loop
while True:
    print('1. For adding a new contact')
    print('2. For deleting a contact')
    print('3. For searching a contact')
    print('4. For exiting the program')

    choice = input('Enter your choice: ')
    if choice == '1':
        user_name = input('Enter your name: ')
        user_phone = input('Enter your phone number: ')
        add_contact(user_name, user_phone)
    elif choice == '2':
        name = input('Enter the name of the contact: ')
        delete_contact(name)
    elif choice == '3':
        name = input('Enter the name of the contact: ')
        search_contact(name)
    elif choice == '4':
        print('Thank you!')
    else:
        print('Invalid input')
    break
