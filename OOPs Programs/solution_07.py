# Static method

"""
Add a static method to the Car class that returns a general description of a car.
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
        self.model = model

    @staticmethod
    def general_desc():
        """
        Return a general description of cars.
        
        Returns:
        str: A description of cars.
        """
        return "Cars are means of transport."
    
# Create instances of the car class
my_car = Car("Toyota", "Corolla")
my_new_car = Car("Tata", "Safari")

# Call the static method using the class name
print(Car.general_desc())