# Task 2: Demonstrating different exceptions

# IndexError example
try:
    my_list = [1, 2, 3]
    print(my_list[5])  # Index 5 does not exist
except IndexError:
    print("IndexError occurred! List index out of range.")

# KeyError example
try:
    my_dict = {"name": "Benita", "age": 22}
    print(my_dict["gender"])  # 'gender' key does not exist
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")

# TypeError example
try:
    result = "5" + 10  # Can't add str and int
except TypeError:
    print("TypeError occurred! Unsupported operand types.")
