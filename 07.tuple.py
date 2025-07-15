# Tuple Basically Immutable

# syntax :my_tuple = (item1, item2, item3)
# | Method     | Description                                          | Example                  |
# | ---------- | ---------------------------------------------------- | ------------------------ |
# | `count(x)` | Returns the number of times `x` appears in the tuple | `t.count(2)` → `2`       |
# | `index(x)` | Returns the first index of value `x`                 | `t.index("apple")` → `0` |


fruits = ("banana","apple","grapes")

f1=fruits.index("apple")

print(f1)

new_fruits = ("guava","watermelon","berry")

f2 = fruits + new_fruits
print(f2)

mix_fruits = f2+ fruits

print(mix_fruits)

f3= mix_fruits.count("apple")
print(f3)

f4 = len(mix_fruits)
print(f4)