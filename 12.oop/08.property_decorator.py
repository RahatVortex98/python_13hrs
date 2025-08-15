# Use Property decorator in the Car class to make model
# attribute read-only



class Car:
    total_car=0
    # bluePrint
    def __init__(self,brand,model):
        self.brand =brand
        self.__model =model
        Car.total_car+=1
 

    # method
    def fullname(self):
        return f"The name of car {self.brand} and it is {self.model}"

    # Polymorphism method:
    def fuel_type(self):
        return f"U need Petrol or Disel?"
    
    # StaticMethod:

    @staticmethod
    def general_description():
        return "Toyota's Gt-86 most powerful racing car in his history!"

    # Property Method:
    @property
    def model(self):
        return self.__model


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
     

print(Car.total_car)

# static method action

print(Car.general_description())
print(my_car.general_description())

print(my_electric_car.general_description())
print(ElectricCar.general_description())

print(my_car.model)