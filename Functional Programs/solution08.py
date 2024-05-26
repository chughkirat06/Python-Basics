# Function with **kwargs

"""
Create a function that accepts any number of keyword arguments and prints them in the format key: value.
"""

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name = "Spider-Man", power = "Web")
print_kwargs(power = "Web")
print_kwargs(name = "Spider-Man", power = "Web", enemy = "Dr. Octopus")