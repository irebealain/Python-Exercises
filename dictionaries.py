# 1. **Create a Contact Book:**
#    - Write a program that uses a dictionary to store names and phone numbers.
#     The program should allow the user to add a new contact, delete a contact,
#     and search for a contact by name.
user_input_one = input("Enter your name: ")
user_input_two = input("Enter your phone number: ")
# Dictionary that stores the names and the phone number.
user_info_dictionary = {"Your names": user_input_one, "Phone number": user_input_two}
for value in user_info_dictionary:
    print(f" {value} : {user_info_dictionary[value]}")


# Allow the user to delete
def delete_contacts():
    user_quest = input("Do you want to delete the contacts? (yes/no): ")
    if user_quest == "yes":
        user_info_dictionary.clear()
        print(f" Your contacts have been deleted.")
    elif user_quest == "no":
        print(f"Thanks for not deleting your contacts 👍")
    else:
        print("Please enter either 'yes' or 'no'")


# print(delete_contacts())


#  Add a new contact
def add_new_contact():
    user_quest = input("Do you want to add a new contact? (yes/no): ")
    if user_quest == "yes":
        add_new_contacts = user_info_dictionary.get(user_input_one)
        print(f"{add_new_contacts}")
        print(f" Your contacts have been added.")


print(f"{user_info_dictionary.get(user_input_one)}")
add_new_contact()
# 2. **Count Word Frequency:**
#    - Write a program that counts the frequency of each word in a given text.
#    Use a dictionary where the keys are words and the values are their counts.
# 3. **Translate Words:**
#    - Create a simple dictionary-based translator.
#    The user can input a word, and if it exists in the dictionary, the program will output the translation.
#    If not, it will prompt the user to add the translation.
#
# 4. **Shopping Cart:**
#    - Write a program that simulates a shopping cart.
#    Use a dictionary where the keys are item names and the values are their prices.
#    Allow the user to add, remove, and view items in the cart, as well as calculate the total cost.
