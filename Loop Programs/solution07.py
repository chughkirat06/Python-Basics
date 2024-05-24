# Validate input

"""
Keep asking the user for input until they enter a number between 1 and 10.
"""

while True:
    try:
        number = int(input("Enter a number: "))
        if 1<= number <= 10:
            print(number)
            break
        else:
            print("Enter a number between 1 - 10")
    except ValueError:
        print("Invalid! Enter an integer between 1 - 10.")
