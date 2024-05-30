# Encapsulation

"""
Modify the car class to encapsulate the brand attribute, making it private,
and provide a getter an setter method for it.
"""

class Car:
    def __init__(self, brand, model):
        """
        Initialize  new car object.

        Parameters:
        brand (str): The brand of the car.
        model (str): The model of the car.
        """
        self.__brand = brand
        self.model = model

    def get_brand(self):
        """
        Get the brand of the car.

        Returns:
        str: The brand of the car.
        """
        return self.__brand
    
    def set_brand(self, brand):
        """
        Set the brand of the car.

        Parameters:
        brand (str): The new brand of the car
        """
        self.__brand = brand

# Create instances of the car class
my_car = Car("Toyota", "Corolla")
my_new_car = Car("Tata", "Safari")

# Print the attributes of the instances
# print(my_car.__brand)     -> Object cannot access private attributes directly
print(my_car.model)
# print(my_new_car.__brand)   -> Object cannot access private attributes directly
print(my_new_car.model)

# Print the private attributes of the instances using getter method
print(my_car.get_brand())
print(my_new_car.get_brand())

# Modify the private attributes of the instances using the setter method
my_car.set_brand("Honda")
my_new_car.set_brand("Mahindra")

# Print the updated private attributes of the instances
print(my_car.get_brand())
print(my_new_car.get_brand())
