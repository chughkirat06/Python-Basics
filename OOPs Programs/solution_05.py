# Polymorphism

"""
Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes,
but with different behaviors
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

    def fuel_type(self):
        """
        Return the fuel type of the car.

        Returns:
        str: The fuel type of the car.
        """
        return "Fuel or Diesel"

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

    def fuel_type(self):
        """
        Return the fuel type of the car.

        Returns:
        str: The fuel type of the car.
        """
        return "Electric charge"

# Create instances of the car class
my_car = Car("Toyota", "Corolla")
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print(my_car.fuel_type())
print(my_tesla.fuel_type())