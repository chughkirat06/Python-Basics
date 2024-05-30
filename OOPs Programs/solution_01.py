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

    def __str__(self) -> str:
        """
        Returna string representation of the car object.

        Returns:
        str: A string describing the car
        """
        return f"Brand: {self.brand}, Model: {self.model}"

# Create instances of the car class
my_car = Car("Toyota", "Corolla")
my_new_car = Car("Tata", "Safari")

# Print the attributes of the instances
print(my_car.brand)
print(my_car.model)
print(my_new_car.brand)
print(my_new_car.model)

# Print the string representation of the instances
print(my_car)
print(my_new_car)