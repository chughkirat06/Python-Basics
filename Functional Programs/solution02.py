# Function with multiple parameters

"""
Create a function that takes two numbers as parameters and returns their sum.
"""

def calculate_sum(num1, num2):
    return num1 + num2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = calculate_sum(num1, num2)
print(result)