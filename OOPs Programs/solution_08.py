# Property decorators

"""
Use a property decorator in the Car class to make the model attribute read-only.
"""

class Car:
    def __init__(self, brand, model):
        """
        Initialize  new car object.

        Parameters:
        brand (str): The brand of the car.
        model (str): The model of the car.
        """
        self.brand = brand
        self.__model = model

    @property
    def model(self):
        """
        The model of the car.
        This atribute is read-only.
        """
        return self.__model

# Create instances of the car class
my_car = Car("Toyota", "Corolla")

# Uncommecting the following line will raise an AttributeError
# because 'model' is read-only
# my_car.model = "City"

# Print the attributes of the instances
print(my_car.brand)
print(my_car.model)