# Class method and self

"""
Add a method to the car class that displays the full name of the car (brand and model)
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
        Return string representation of the car object.

        Returns:
        str: A string describing the car.
        """
        return f"Brand: {self.brand}, Model: {self.model}"
    
    def full_name(self):
        """
        Returns the full anme of the car object.

        Returns:
        str: A string describing the full name of the car.
        """
        return f"{self.brand} {self.model}"

# Create instances of the car class
my_car = Car("Toyota", "Corolla")
my_new_car = Car("Tata", "Safari")

# Print the attributes of the instances
print(my_car.brand)
print(my_car.model)
print(my_new_car.brand)
print(my_new_car.model)

# Print the full name of the Car instances
print(my_car.full_name())
print(my_new_car.full_name())

# Print the string representation of the instances
print(my_car)
print(my_new_car)