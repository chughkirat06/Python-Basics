# Inheritance

"""
Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
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
        super().__init__(brand, model)
        self.battery_size = battery_size

# Create instances of the car class
my_car = Car("Toyota", "Corolla")
my_new_car = Car("Tata", "Safari")
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# Print the attributes of the instances
# print(my_car.brand)
# print(my_car.model)
# print(my_new_car.brand)
# print(my_new_car.model)
print(my_tesla.brand)
print(my_tesla.model)
print(my_tesla.battery_size)

# Print the string representation of the instances
# print(my_car)
# print(my_new_car)
print(my_tesla)