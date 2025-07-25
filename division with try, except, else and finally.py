# Task 3: Division with try, except, else, and finally

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Oops! Division by zero is not allowed.")
except ValueError:
    print("Invalid input! Please enter numbers only.")
else:
    print(f"The result is {result}.")
finally:
    print("This block always executes.")
