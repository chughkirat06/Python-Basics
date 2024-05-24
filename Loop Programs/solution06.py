# Factorial calculator

"""
Compute the factorial of a number using a while loop
"""

# Get number from user
while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Please enter a valid integer number.")

# Check if user input is a negative number
if number < 0:
    print("Factorial is not defined for negative number.")
    exit()

factorial = 1

# Compute factorial
while number > 0:
    factorial *= number
    number -= 1

print(factorial)