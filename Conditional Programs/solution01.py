# Age group categorization

"""
Classify a person's age group:
Child (< 13),
Teenager (13-19),
Adult (20-59),
Senior (60+)
"""

user_age = int(input("Provide an age: "))

if user_age < 13:
    print("Child")
elif user_age < 20:
    print("Teenager")
elif user_age < 60:
    print("Adult")
else:
    print("Senior")