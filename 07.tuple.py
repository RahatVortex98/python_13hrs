# Tuple Basically Immutable

# syntax :my_tuple = (item1, item2, item3)
# | Method     | Description                                          | Example                  |
# | ---------- | ---------------------------------------------------- | ------------------------ |
# | `count(x)` | Returns the number of times `x` appears in the tuple | `t.count(2)` → `2`       |
# | `index(x)` | Returns the first index of value `x`                 | `t.index("apple")` → `0` |

fruits = ("banana", "apple", "grapes")

f1 = fruits.index("apple")      # Finds index of "apple" → 1
print(f1)                       # Output: 1

new_fruits = ("guava", "watermelon", "berry")

f2 = fruits + new_fruits        # Tuples are immutable, but you can concatenate
print(f2)                       # Output: ('banana', 'apple', 'grapes', 'guava', 'watermelon', 'berry')

mix_fruits = f2 + fruits        # More concatenation → creates a new tuple
print(mix_fruits)               # Output: full combined tuple

f3 = mix_fruits.count("apple") # Counts how many times "apple" appears
print(f3)                       # Output: 2

f4 = len(mix_fruits)           # Length of the tuple
print(f4)                       # Output: 9
