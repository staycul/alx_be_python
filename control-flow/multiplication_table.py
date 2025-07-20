# File: control-flow/multiplication_table.py

# Prompt user for input
try:
    number = int(input("Enter a number to see its multiplication table: "))

    # Generate multiplication table from 1 to 10
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")
except ValueError:
    print("Please enter a valid integer.")
