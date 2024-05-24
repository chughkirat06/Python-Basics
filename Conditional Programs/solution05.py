# Weather activity suggestion

"""
Suggest an activity based on the weather 
(e.g., Sunny - Go for a walk, 
Rainy - Read a book,
Snowy - Build a snowman)
"""

# Dictionary mapping weather conditions to activities
weather_list = {
    "sunny": "Go for a walk",
    "rainy": "Read a book",
    "snowy": "Build a snowman"
}

# Get weather from user
weather = input("Enter weather (sunny, rainy, snowy): ").strip().lower()

# Suggest activity based on weather condition
if weather in weather_list:
    activity = weather_list[weather]
    print(activity)
else:
    print("Weather not recognized. Please enter sunny, rainy, or snowy.")