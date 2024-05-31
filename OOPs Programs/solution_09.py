# Class inheritance and isinstance() function

"""
Demonstarte the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.
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

    def __str__(self) -> str:
        """
        Return string representation of the car object.

        Returns:
        str: A string describing the car.
        """
        return f"{self.brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        """
        Initialize a new ElectricCar object.

        Parameters:
        brand (str): The brand of the car.
        model (str): The model of the car.
        battery_size (str): The battery size of the electric car.
        """
        super().__init__(brand, model)
        self.battery_size = battery_size

# Create instances of the car class
my_car = Car("Toyota", "Corolla")
my_new_car = Car("Tata", "Safari")
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# Check instances using isinstance()
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))
