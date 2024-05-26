# Function returning multiple values

"""
Create a function that returns both the area and circumference of a circle given its radius.
"""

import math

def calculate_circle_stats(radius):
    """
    Calculate area and circumference of a circle.

    Parameters:
    radius (float): The value used to calculate the circle stats.

    Returns:
    Tuple[float, float]: A tuple containing the area and circumference of the circle.
    """
    if radius <= 0:
        raise ValueError("Radius nust be a positive number.")
    
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    return area, circumference

def main():
    try:
        radius = float(input("Enter the radius of the circle: "))
        area, circumference = calculate_circle_stats(radius)
        print(f"Area: {area:.2f} Circumference: {circumference:.2f}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()