# 4. **Shopping Cart:**
#    - Write a program that simulates a shopping cart.
#    Use a dictionary where the keys are item names and the values are their prices.
#    Allow the user to add, remove, and view items in the cart, as well as calculate the total cost.
# A dictionary with all the fruits in it.
shopping_dict = {
    'apple': 2.00,
    'banana': 4.00,
    'cherry': 5.00,
    'mango': 6.00,
    'orange': 1.00,
    'strawberry': 9.00
}


# A function to add new fruit.
def add_to_cart(items, tag):
    shopping_dict[items] = tag
    print(shopping_dict)


# A function to add new fruit.
def del_from_cart(item):
    if item in shopping_dict:
        del shopping_dict[item]
        print("The fruit has been deleted successfully")
        print(shopping_dict)
    else:
        print("The fruit is not in the cart")
        print(shopping_dict)


# A function to search the fruit in the dictionary.
def search_cart(fruits):
    if fruits in shopping_dict:
        print(f" The {fruits} has been found")
    else:
        print("The fruit is not in the cart")
def calculate_total_price(items):
    shopping_dict.values()
# Looping through options.
while True:
    print("What would you like to do?")
    print("1. Add a fruit")
    print("2. Delete a fruit")
    print("3. Search a cart")
    print("4. Calculate the total price")

    choice = input("Enter your choice: ")
    if choice == "1":
        fruit = input("Enter a fruit: ")
        price = input("Enter a price: ")
        add_to_cart(fruit, price)
    elif choice == "2":
        fruit = input("Enter a fruit: ")
        del_from_cart(fruit)
    elif choice == "3":
        fruit = input("Enter a fruit: ")
        search_cart(fruit)
    elif choice == "4":
        total_price()
        print("Thank you!")
    else:
        print("Invalid input")
    break
