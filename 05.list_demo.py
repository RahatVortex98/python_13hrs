# 🔧 Common Methods:
# append() – Add an item at the end
# insert() – Add an item at a specific index
# remove() – Remove the first occurrence of a value
# pop() – Remove an item by index (default is last)
# sort() – Sort the list
# reverse() – Reverse the list
# len() – Returns the number of items in the list

# ✅ Mutable: You can change, add, or remove items after the list has been created.

tea = ['Herbal','Green','Lemon','Black']

print(tea)             # ['Herbal', 'Green', 'Lemon', 'Black']
print(tea[1])          # Accessing 2nd item → 'Green'
print(tea[1:2])        # Slicing → ['Green'] (list with one item)

tea[1:2] = 'Oolong'    # Replacing slice with string → inserts each character of 'Oolong'
print(tea)             # ['Herbal', 'O', 'o', 'l', 'o', 'n', 'g', 'Lemon', 'Black']

tea = ['Herbal','Green','Lemon','Black']  # Reset the list to original
print(tea)

tea[1:2] = ['Oolong']  # Replace second item with a list → keeps structure intact
print(tea)             # ['Herbal', 'Oolong', 'Lemon', 'Black']

print(tea[1:1])        # Empty slice → []

tea[1:1] = ["Masala"]  # Insert 'Masala' at index 1 (before 'Oolong')
print(tea)             # ['Herbal', 'Masala', 'Oolong', 'Lemon', 'Black']

if "Oolong" in tea:    # Membership check
    print(" yes oolong availble")  # Output: yes oolong availble

tea1 = ['Herbal','Green','Lemon','Black']
for tea in tea1:       # Iterating through each item in list
    print(tea)         # Prints: Herbal, Green, Lemon, Black

tea1.append('milk')    # Adds 'milk' at the end
print(tea1)            # ['Herbal', 'Green', 'Lemon', 'Black', 'milk']

tea1.pop()             # Removes last item (milk)
print(tea1)            # ['Herbal', 'Green', 'Lemon', 'Black']

tea1.remove("Black")   # Removes 'Black' by value
print(tea1)            # ['Herbal', 'Green', 'Lemon']

tea1.insert(1,'milk')  # Inserts 'milk' at index 1
print(tea1)            # ['Herbal', 'milk', 'Green', 'Lemon']

tea = ['Herbal','Green','Lemon','Black']
tea2 = tea.copy()      # Shallow copy → new memory address, same values
print(tea2)            # ['Herbal', 'Green', 'Lemon', 'Black']

#Range(10) ==>0 1 2 3 4 5 6 7 8 9

square_number = [x**2 for x in range(10)]   # List comprehension to get squares
print(square_number)                        # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

cube_number = [x**3 for x in range(3)]      # Cubes of 0,1,2
print(cube_number)                          # [0, 1, 8]
