# Basic function syntax

"""
Write a function to calculate and return the square of a number.
"""

def calculate_square(number: int) -> int:
    """
    Calculate and return the square of a number.

    Parameters:
    number (int): The number to be squared.

    Returns:
    int: The square of the given number.
    """
    return number ** 2

def main():
    try:
        number = int(input("Enter a number to find the square: "))
        result = calculate_square(number)
        print(f"The square of {number} is {result}.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()