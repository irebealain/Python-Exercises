# 1. **Print Even Numbers:**
#    - Write a program that prints all even numbers from 1 to 100 using a loop.
even_numbers = []


def display_even_numbers():
    number_limit = 101
    for num in range(0, number_limit):
        if num % 2 == 0:
            even_numbers.append(num)
    print(even_numbers)


display_even_numbers()


