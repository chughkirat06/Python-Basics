# Default parameter value

"""
Write a function that greets a user. If no name is provided, it should greet with a default name.
"""

def greet_user(name = "User"):
    return "Welcome, " + name + "!"

message = greet_user("kirat")
print(message)
print(greet_user())