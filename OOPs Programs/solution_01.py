# Basic class and object

"""
Create a car class with attributes like brand and model.
Then create an instance of this class.
"""

class Car:
    def __init__(self, brand, model):
        """
        Initialize a new car object.

        Parameters:
        brand (str): The brand of the car.
        model (str): The model of the car.
        """
        self.brand = brand
        self.model = model

# Create instances of the car class
my_car = Car("Toyota", "Corolla")
my_new_car = Car("Tata", "Safari")

# Print the attributes of the instances
print(my_car.brand)
print(my_car.model)
print(my_new_car.brand)
print(my_new_car.model)
