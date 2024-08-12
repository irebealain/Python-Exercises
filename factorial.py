def calc_factorial():
    user_input = int(input("Enter a number: "))
    factorial = 1
    for num in range(1, user_input + 1):
        factorial *= num
    print(f"The factorial of {user_input} is {factorial}")


calc_factorial()
