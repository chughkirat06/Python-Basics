#  Movie ticket pricing

"""
Movie tickets are priced based on age:
$12 for adults (18 and over),
$8 for children.
Everyone gets a $2 discount on Wednesday.
"""

from datetime import datetime

# Get current system date and time 
now = datetime.now()

# Get the day of the week
day_of_week = now.strftime("%A")

# Get user age
try:
    user_age = int(input("Provide age: "))
except ValueError:
    print("Invalid input. Please enter a valid age.")
    exit()

# Set movie ticket price
# if user_age >= 18:
#     ticket_price = 12
# else:
#     ticket_price = 8
ticket_price = 12 if user_age >= 18 else 8

# Apply discount if today is Wedneday
if day_of_week == "Wednesday":
    ticket_price -= 2

print(f"Your ticket price is: ${ticket_price}")