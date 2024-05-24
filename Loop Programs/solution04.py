# Reverse a string

"""
Reverse a string using loop
"""

# Get string from user
input_str = input("Provide your string here: ")
reversed_str = ""

# Reverse string
for char in input_str:
    reversed_str = char + reversed_str

print(reversed_str)
