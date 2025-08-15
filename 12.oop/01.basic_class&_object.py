# Create a car class with attributes like brand and model.
# Then create an instance of this class.

# Attribute
# An attribute is a variable that belongs to an object.

# __init__ Method
# __init__ is the constructor in Python classes.

# Runs automatically when you create a new object.


# | Term       | Meaning                                            |
# | ---------- | -------------------------------------------------- |
# | `self`     | Refers to the current object                       |
# | Attribute  | Variable that belongs to an object                 |
# | `__init__` | Special method that runs when an object is created |


class Car:  # Create a class blueprint for Car objects
    def __init__(self, brand, model):  # Constructor, runs when a new Car is created
        self.brand = brand  # Store brand as an attribute in the object
        self.model = model  # Store model as an attribute in the object

my_car = Car("Toyota", "Gt-86")  # Create first Car object with Toyota and Gt-86
print(my_car.brand)  # Access brand → Toyota
print(my_car.model)  # Access model → Gt-86

my_new_car = Car("Hyundai", "Grace")  # Create second Car object with Hyundai and Grace
print(my_new_car.model)  # Access model → Grace
