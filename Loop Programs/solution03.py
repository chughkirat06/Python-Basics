# Multiplication table printer

"""
Print the multiplication table for a given number upto 10,
but skip the fifth iteration.
"""

# Get number from user for multiplication
try:
    number = int(input("Enter value: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

# Multiplication table
for n in range(1, 11):
    value = number * n
    if n == 5:
        continue
    print(f"{number} x {n} = {value}") 