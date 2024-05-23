# Fruit ripeness checker

"""
Determine if a fruit is ripe, overrirpe, or unripe based on its color. 
(e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)
"""

# Dictionary mapping fruits to their color ripeness
color_criteria = {
    "banana": {
        "green": "Unripe",
        "yellow": "Ripe",
        "brown": "Overripe"
    },
    "apple": {
        "green": "Unripe",
        "red": "Ripe",
        "brown": "Overripe"
    },
    "grape": {
        "yellow": "Unripe",
        "green": "Ripe",
        "brown": "Overripe"
    }
}

# Get fruit from user
fruit = input("Enter the fruit name (e.g., Banana, Apple, Grape): ").strip().lower()

# Check if fruit is in the dictionary
if fruit in color_criteria:
    # Get fruit color from user
    fruit_color = input("Provide fruit color: ").strip().lower()
    color_ripeness = color_criteria[fruit].get(fruit_color, "Color not recodnized")
    print(color_ripeness)
else:
    print("Fruit not recognized")