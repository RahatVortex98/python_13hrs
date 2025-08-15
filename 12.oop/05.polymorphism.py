# Demonstrate polymorphism by defining a mthod
# fuel_type in both Car and ElectricCar classes,But
# different behaviors.


# polymorphism==
#  means “same method name, different behavior,” 
# depending on the object (or class) calling it.

class Car:
    # bluePrint
    def __init__(self,brand,model):
        self.brand =brand
        self.model =model
 

    # method
    def fullname(self):
        return f"The name of car {self.brand} and it is {self.model}"

    # Polymorphism method:
    def fuel_type(self):
        return f"U need Petrol or Disel?"


# Create Object
my_car=Car('Toyota','gt-86')

print(my_car.brand)
print(my_car.model)
# Calling the method by using 1st object
print(my_car.fullname())


# Inherite 

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        self.battery_size =battery_size
        super().__init__(brand, model)

     # Polymorphism method:
    def fuel_type(self):
        return f"U need charging Plug?"

my_electric_car=ElectricCar('Tesla','M','20kw')

print(my_electric_car.brand)
print(my_electric_car.model)
print(my_electric_car.battery_size)

# calling parent Class method
print(my_electric_car.fullname())


 

# Ploymorphism method call both class

print(my_car.fuel_type())

print(my_electric_car.fuel_type())
     