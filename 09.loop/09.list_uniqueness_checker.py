# Check if all elements in a list are unique. if duplicate found exit the loop and print duplicate.

items=["apple","banana","orange","apple","mango"]

unique = set()

for i in items:
    if i in unique:
        print(i)
        break
    unique.add(i)


