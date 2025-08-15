# Demonstrate the use isinstance() to check if my_tesla is
# is an instance if Car and ElectricCar


class Car:
    total_car = 0
    
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model   # Private by convention
        Car.total_car += 1

    def fullname(self):
        return f"The name of car {self.brand} and it is {self.model}"

    def fuel_type(self):
        return f"U need Petrol or Diesel?"

    @staticmethod
    def general_description():
        return "Toyota's Gt-86 most powerful racing car in its history!"

    # Read-only property
    @property
    def model(self):
        return self.__model


# Create Object
my_car = Car('Toyota', 'gt-86')

print(my_car.brand)       # "Toyota"
print(my_car.model)       # No () needed now
print(my_car.fullname())  # Uses the property inside fullname()

# Inherit
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        self.battery_size = battery_size
        super().__init__(brand, model)

    def fuel_type(self):
        return f"U need charging Plug?"


my_electric_car = ElectricCar('Tesla', 'M', '20kw')

print(my_electric_car.brand)
print(my_electric_car.model)   # Still read-only
print(my_electric_car.battery_size)
print(my_electric_car.fullname())

print(my_car.fuel_type())
print(my_electric_car.fuel_type())
print(Car.total_car)

# Static method action
print(Car.general_description())
print(my_car.general_description())
print(my_electric_car.general_description())
print(ElectricCar.general_description())

# Trying to modify will fail
# my_car.model = "New Model"  # ❌ AttributeError



# isInstance 

print(isinstance(my_electric_car,Car))
print(isinstance(my_electric_car,ElectricCar))