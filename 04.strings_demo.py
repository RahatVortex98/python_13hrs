# ---------------------------
# STRING IMMUTABLE
# ---------------------------


# 🔧 Common String Methods:
# lower() – Converts all characters to lowercase

# upper() – Converts all characters to uppercase

# strip() – Removes leading and trailing spaces

# replace(old, new) – Replaces part of the string

# split() – Splits the string into a list

# join() – Joins a list into a string

# find() – Returns the index of a substring

# count() – Counts the number of occurrences of a substring

# format() – Formats strings using placeholders

l1 = "Masala Chai"
print(l1[0])  # Accessing first character → 'M'

print(l1[0:6])  # Slicing string → 'Masala' (from index 0 to 5)

# ---------------------------
# STRING SLICING
# ---------------------------

L2 = "0123456789"
print(L2[0:5:2])  # Slice from index 0 to 4, step by 2 → '024'
print(L2[0:-1])   # All except last character → '012345678'

# ---------------------------
# STRING METHODS (UNICODE)
# ---------------------------

print(l1.lower())  # Convert to lowercase → 'masala chai'
print(l1.upper())  # Convert to uppercase → 'MASALA CHAI'

# ---------------------------
# STRING STRIP (removes leading/trailing spaces)
# ---------------------------

l3 = "  Ginger Chai "
print(l3.strip())  # Removes spaces → 'Ginger Chai'

# ---------------------------
# STRING REPLACE
# ---------------------------

l4 = "Lemon Chai"
print(l4.replace("Chai", "tea "))  # Replaces 'Chai' with 'tea ' → 'Lemon tea '

# ---------------------------
# STRING SPLIT
# ---------------------------

l5 = "lemon,Ginger,Masala"
print(l5.split())        # Splits on whitespace (none here) → ['lemon,Ginger,Masala']
print(l5.split(","))     # Splits by comma → ['lemon', 'Ginger', 'Masala']

# ---------------------------
# STRING FIND
# ---------------------------

print(l5.find("lemon"))   # Returns index → 0
print(l5.find("Lemon"))   # Case-sensitive, not found → -1

# ---------------------------
# STRING COUNT
# ---------------------------

l6 = 'lemon chai Ginger chai Masala chai'
print(l6.count("chai"))   # Counts occurrences of 'chai' → 3

# ---------------------------
# STRING FORMAT (placeholder formatting)
# ---------------------------

chai_type = "Milk Tea"
qauntity = 2
order = "i have ordered {} cup of {}"  # {} are placeholders

print(order.format(qauntity, chai_type))  # Inserts values → 'i have ordered 2 cup of Milk Tea'

# ---------------------------
# CONVERT STRING TO LIST & LIST TO STRING
# ---------------------------

# Split: String → List
# Join: List → String

# By using SPLIT we can convert strings to list
# By using "".join(varible_name) we can change list to strings


l7 = ["lemon", "ginger", "clove"]

print(",".join(l7))  # Joins with commas → 'lemon,ginger,clove'

# ---------------------------
# STRING LENGTH
# ---------------------------

print(len(l5))  # Length of l5 → 20 (includes commas)



