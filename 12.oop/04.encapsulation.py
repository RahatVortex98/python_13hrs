# modify the Car class to encapsulate the brand attribute
# making it private and provide a getter method for it.

# A getter is a method (or mechanism) in object-oriented programming that is used to access (or get) the value of an object's attribute.



class Car:
    # Blueprint for creating Car objects
    def __init__(self, brand, model):
        self.__brand = brand   # private attribute (double underscore)
        self.model = model     # public attribute

    # Getter method to access private brand
    def get_brand(self):
        return self.__brand

    # Method to return full car name
    def fullname(self):
        return f"The name of car {self.__brand} and it is {self.model}"


# Create first Car object
my_car = Car('Toyota', 'gt-86')

# Access brand using the getter (cannot do my_car.__brand directly)
print(my_car.get_brand())  # Toyota
print(my_car.model)        # gt-86

# Call method
print(my_car.fullname())   # The name of car Toyota and it is gt-86


# Child class inheriting from Car
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        self.battery_size = battery_size
        # Call parent constructor to set brand and model
        super().__init__(brand, model)

# Create ElectricCar object
my_electric_car = ElectricCar('Tesla', 'Model S', '20kWh')

# Access brand via getter
print(my_electric_car.get_brand())  # Tesla
print(my_electric_car.model)        # Model S
print(my_electric_car.battery_size) # 20kWh

# Call parent method
print(my_electric_car.fullname())   # The name of car Tesla and it is Model S
