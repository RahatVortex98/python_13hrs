# Create an electricCar class that inherts from the Car class and 
# has an additional attribute battery size.

class Car:  # Create a Car class (blueprint for creating car objects)
    def __init__(self, brand, model):  # Constructor method, runs when a new object is made
        self.brand = brand  # Store the brand in the object
        self.model = model  # Store the model in the object

    # Method: function that belongs to the class
    def full_name(self):  
        # Return a string using the brand and model of this object
        return f"The full name of the car {self.brand} and {self.model}"

# Create first Car object
my_car = Car("Toyota", "Corolla")

# Access attributes of my_car
print(my_car.brand)  # Toyota
print(my_car.model)  # Corolla

# Call the full_name() method of my_car
print(my_car.full_name())  # The full name of the car Toyota and Corolla

# Create second Car object
my_new_car = Car("Mercedes", "GLS-450")

# Access attributes of my_new_car
print(my_new_car.brand)  # Mercedes
print(my_new_car.model)  # GLS-450



# Inhertance
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

    def about(self):
        return f"About my new Car name is {self.brand}{self.model} and it has {self.battery_size}"

my_electric_car=ElectricCar('Tesla','496','2000mah')
print(my_electric_car.brand)
print(my_electric_car.model)
print(my_electric_car.battery_size)

print(my_electric_car.about())