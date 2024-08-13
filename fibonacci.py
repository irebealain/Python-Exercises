# 4. **Fibonacci Sequence:**
#    - Write a program that prints the first `n` numbers of the Fibonacci sequence, where `n` is input by the user.
# These exercises should help you practice and improve your understanding of dictionaries, OOP, and loops in Python.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
user_input = int(input("Please enter the number of times for fibonacci: "))


def fibonacci(limit):
    fib = [0, 1]
    for i in range(2, limit):
        fib.append(fib[i - 1] + fib[i - 2])
    print(fib)


fibonacci(user_input)
