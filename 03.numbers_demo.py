# Identity check: two separate lists with same content but different memory locations
m = [1, 2, 3]
n = [1, 2, 3]
print(m is n)  # False, because m and n are different objects in memory

# Integers (small ones) are cached in Python, so a and b point to same memory
a = 5
b = 5
print(a is b)  # True

# Variables and basic arithmetic
x = 2
y = 3
z = 4

print(x + y)  # 2 + 3 = 5

# Float and int addition
print(40 + 2.23)  # = 42.23 (float + int = float)

# Explicit type conversion from float to int (2.23 becomes 2)
print(40 + int(2.23))  # = 42

# Printing multiple values
print(x, y, z)  # 2 3 4

# Expressions inside print
print(x + 1, y * 2)  # 3 6

# Exponentiation (2 to the power of 100)
print(2 ** 100)  # Very large number

# Logical AND: both conditions must be true
print(x < y and y < z)  # True and True → True

# Logical OR: at least one condition is true
print(x < y or y < z)  # True or True → True

# Math library: floor rounds down
import math
print(math.floor(3.5))  # 3

# Random number generation
import random

# Random float between 0 and 1
print(random.random())  

# Random integer between 1 and 10 (inclusive)
print(random.randint(1, 10))  

# Random selection from a list
l1 = ['lemon', 'masala', 'ginger']
print(random.choice(l1))  

# Shuffle list items in place (changes l2 directly)
l2 = ['lemon', 'masala', 'ginger']
random.shuffle(l2)  # no return value, modifies l2
print(l2)  # prints shuffled version of l2

# Fractions module for exact fraction representation
from fractions import Fraction
myFra = Fraction(2, 7)  # creates a fraction 2/7
print(myFra)  # Output: 2/7
