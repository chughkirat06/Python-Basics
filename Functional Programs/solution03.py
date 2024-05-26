# Polymorphism in functions

"""
Write a function multiply that multiplies two numbers, 
but can also accept and multiply strings.
"""

def calculate_multiple(value1, value2):
    return value1 * value2

result1 = calculate_multiple(1, 2)
result2 = calculate_multiple('a', 5)
print(result1)
print(result2)