from EMS import Employee

user_one = Employee('John', 123, 'Finance')

# user_one.add_employee('Alain', 765)
user_two = Employee('Jack', 456, 'Python')
# user_two.remove_employee('Jack')
user_three = Employee('Jane', 124, 'Logistics')
user_three.display()
user_one.remove_employee()
user_four = Employee('Jack', 125, 'Operations')