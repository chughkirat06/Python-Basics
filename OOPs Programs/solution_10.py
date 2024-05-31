# Multiple inheritance

"""
Create two classes Battery and Motor, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.
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
    
class Battery:
    def __init__(self, energy_capacity):
        self.energy_capacity = energy_capacity

    def battery_count(self):
        return "Powerwall 3 batteries"

class Motor:
    def __init__(self, motor_output):
        self.motor_output = motor_output

    def motor_type(self):
        return "Induction motor"

class ElectricCar(Car, Battery, Motor):
    def __init__(self, brand, model, battery_size, energy_capacity, motor_output):
        """
        Initialize a new ElectricCar object.

        Parameters:
        brand (str): The brand of the car.
        model (str): The model of the car.
        battery_size (str): The battery size of the electric car.
        energy_capacity (str): The energy capacity of the electric car.
        motor_output (str): The motor output of the electric car.
        """
        Car.__init__(self, brand, model)
        Battery.__init__(self, energy_capacity)
        Motor.__init__(self, motor_output)
        self.battery_size = battery_size

# Create instances of the car class
my_new_tesla = ElectricCar("Tesla", "Model S", "85kWh", "54kWh", "825 hp")

# Print the attributes of the instances
print(my_new_tesla.brand)
print(my_new_tesla.model)
print(my_new_tesla.battery_size)
print(my_new_tesla.energy_capacity)
print(my_new_tesla.motor_output)
print(my_new_tesla.motor_type())
print(my_new_tesla.battery_count())
