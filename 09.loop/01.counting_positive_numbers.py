#  given a list of numbers count how many are positive.

numbers =[1,-2,3,-4,5,6,-7,-8,9,10]

count=0

for number in numbers:
     if number >0:
        count +=1
print('final total positive number :',count)




# | Step | number | number > 0? | count before | count after |
# | ---- | ------ | ----------- | ------------ | ----------- |
# | 1    | 1      | ✅ yes       | 0            | 1           |
# | 2    | -2     | ❌ no        | 1            | 1           |
# | 3    | 3      | ✅ yes       | 1            | 2           |
# | 4    | -4     | ❌ no        | 2            | 2           |
# | 5    | 5      | ✅ yes       | 2            | 3           |
# | 6    | 6      | ✅ yes       | 3            | 4           |
# | 7    | -7     | ❌ no        | 4            | 4           |
# | 8    | -8     | ❌ no        | 4            | 4           |
# | 9    | 9      | ✅ yes       | 4            | 5           |
# | 10   | 10     | ✅ yes       | 5            | 6           |
