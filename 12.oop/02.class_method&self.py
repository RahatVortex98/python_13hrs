# Add a method to the car class that displays 
# the full name of the car(brand and model.)



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
