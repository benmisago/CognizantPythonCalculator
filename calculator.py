import logging

# Step 4: Set up logging to file
logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError as ve:
            print("Invalid input! Please enter a valid number.")
            logging.error(f"ValueError occurred: {ve}")

def perform_operation(choice):
    if choice in [1, 2, 3, 4]:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        try:
            if choice == 1:
                result = num1 + num2
                print(f"The result of addition is: {result}")
            elif choice == 2:
                result = num1 - num2
                print(f"The result of subtraction is: {result}")
            elif choice == 3:
                result = num1 * num2
                print(f"The result of multiplication is: {result}")
            elif choice == 4:
                result = num1 / num2
                print(f"The result of division is: {result}")
        except ZeroDivisionError as zde:
            print("Oops! Division by zero is not allowed.")
            logging.error(f"ZeroDivisionError occurred: {zde}")
        except Exception as e:
            print("An unexpected error occurred.")
            logging.error(f"Unexpected error: {e}")
        else:
            print("Operation completed successfully.")
        finally:
            print("Returning to the main menu...\n")

def display_menu():
    print("\nWelcome to the Error-Free Calculator!")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("> "))
            if choice == 5:
                print("Goodbye!")
                break
            elif choice in [1, 2, 3, 4]:
                perform_operation(choice)
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
        except Exception as e:
            print("Something went wrong.")
            logging.error(f"Unexpected error in main loop: {e}")

if __name__ == "__main__":
    main()
