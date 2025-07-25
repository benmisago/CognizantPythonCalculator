# Task 1: Divide 100 by user input with exception handling

while True:
    try:
        user_input = input("Enter a number: ")
        number = float(user_input)
        result = 100 / number
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    else:
        print(f"100 divided by {number} is {result}")
        break
