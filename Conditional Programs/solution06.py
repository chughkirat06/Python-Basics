# Transportation mode selection

"""
Choose a mode of transportation based on the distance
(e.g., <3 km: Walk,
3-15 km: Bike,
>15 km: Car)
"""

def get_transportation_mode(distance):
    """
    Determines the mode of transportation based on the given distance.

    Parameters:
    distance (int): The distance in kilometers.

    Returns:
    str: The mode of transportation.
    """
    if distance < 3:
        return "Walk"
    elif distance <= 15:
        return "Bike"
    else:
        return "Car"

def main():
    try:
        # Get distance from user
        distance = int(input("Enter distance in kms: "))
        # Determine the mode of transportation
        mode = get_transportation_mode(distance)
        print(mode)
    except ValueError:
        print("Enter valid distance in kms.")
    exit()

if __name__ == "__main__":
    main()
