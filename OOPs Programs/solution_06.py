# Class variables

"""
Add a class variable to Car that keeps track of the number of cars created.
"""

class Car:
    """
    A class to represent a car.

    Attributes:
    total_car (int): Class variable to keep track of the number of car instances created.
    """
    
    total_car = 0

    def __init__(self, brand, model):
        """
        Initialize  new car object.

        Parameters:
        brand (str): The brand of the car.
        model (str): The model of the car.
        """
        self.brand = brand
        self.model = model
        Car.total_car += 1

# Create instances of the car class
my_car = Car("Toyota", "Corolla")
my_new_car = Car("Tata", "Safari")

# Print the total number of Car instances created
print(f"Total number of cars created: {Car.total_car}")