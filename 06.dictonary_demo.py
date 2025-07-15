# 🔧 Common Dictionary Methods:
# | Method       | Description                              |
# | ------------ | ---------------------------------------- |
# | `get(key)`   | Returns value for the key; avoids error  |
# | `keys()`     | Returns all keys                         |
# | `values()`   | Returns all values                       |
# | `items()`    | Returns all key-value pairs              |
# | `update({})` | Adds or updates multiple key-value pairs |
# | `pop(key)`   | Removes the item with the specified key  |
# | `clear()`    | Removes all items                        |

chai_types = {
    "Masala": "spicy",
    "Ginger": "Zesty",
    "Green": "Mild"
}

print(chai_types)  # {'Masala': 'spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}

if "Masala" in chai_types:  # Checks if 'Masala' is a key
    print("yes availble")

# Loop through keys and print key-value pairs
for chai in chai_types:
    print(chai, chai_types[chai])
    # Output: Masala spicy, Ginger Zesty, Green Mild

print(len(chai_types))  # Number of key-value pairs → 3

chai_types["Earl Grey"] = "Smokey"  # Add new key-value pair
print(chai_types)  # 'Earl Grey': 'Smokey' is added

chai_types.pop("Earl Grey")  # Remove specific key
print(chai_types)

chai_types.popitem()  # Removes last inserted item (Python 3.7+)
print(chai_types)

chai_types_copy = chai_types.copy()  # Shallow copy of the dictionary
print(chai_types_copy)

# Safe value retrieval using get()
searching = chai_types.get('Masala')
print(searching)  # Output: spicy

availble = chai_types.keys()  # Get all keys
print(availble)  # Output: dict_keys(['Masala', 'Ginger'])

# Dictionary comprehension: key → value squared
square_num = {x: x**2 for x in range(10)}
print(square_num)  # {0: 0, 1: 1, ..., 9: 81}

# fromkeys: all values point to the same list reference (⚠️ shared reference!)
bucket = ["Apple", "Banana", "Grapes"]
taste = ["sour", "sweet", "sweetness"]
taste1 = "Sweet"

new_bucket = dict.fromkeys(bucket, taste)
new_bucket1 = dict.fromkeys(bucket, taste1)

print(new_bucket)   # All keys share the same list as value
print(new_bucket1)  # All keys share the same string as value
