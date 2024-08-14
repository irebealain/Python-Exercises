# 2. **Student Grades Tracker:**
#    - Create a `Student` class with attributes for name and a dictionary for grades.
#    - Write methods to add grades, calculate the average grade, and print the student's information.
#    - Use loops to input multiple grades and store them in the dictionary.

class Student:
    def __init__(self, first_name, last_name, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = {
            grade: 89
        }
    def