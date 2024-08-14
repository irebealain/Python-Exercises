# 1. **Employee Management System:**
#    - Create a program that manages employees using OOP and dictionaries.
#    - Create an `Employee` class with attributes like name, ID, and department.
#    - Store employees in a dictionary with their ID as the key.
#    - Implement functions to add, remove, and display employees, and use loops where necessary.
class Employee:
    def __init__(self, name, user_id, department):
        self.employee_dict = {
            "id": user_id,
            "name": name,
            "department": department
        }

    def add_employee(self, name, user_id):
        self.employee_dict[user_id] = name
        print(f"The new employee is {self.employee_dict[user_id]}")

    def remove_employee(self):
        if 'id' in self.employee_dict:
            del self.employee_dict["id"]
            print(f"The employee {self.employee_dict} has been removed")
        else:
            print(f"The employee {self.employee_dict['id']} does not exist")

    def display(self):
        print(self.employee_dict)

#
# 3. **Inventory Management System:**
#    - Create a class `Item` with attributes like name, price, and quantity.
#    - Use a dictionary to store items with the item name as the key.
#    - Implement methods to add items, update quantity, calculate the total inventory value, and display all items.
#    - Use loops to iterate through the dictionary and perform the necessary operations.
