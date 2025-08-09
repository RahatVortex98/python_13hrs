# Given string find the non repeated character


input_strr = 'Hello python '

for i in input_strr:
    if input_strr.count(i)==1:
        print(i)