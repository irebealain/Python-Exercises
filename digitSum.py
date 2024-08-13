user_input = input("Enter a number: ")


def add_digit(num):
    digit_sum = 0
    for digit in num:
        digit_sum += int(digit)
    print(f"The sum of digits of {user_input} is {digit_sum}")


add_digit(user_input)
