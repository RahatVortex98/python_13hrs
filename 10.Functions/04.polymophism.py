# The ability of different data types to respond to the same method or function call in a way that is specific to their type.


# write a function multiply that multiplies two numbers,but can also accept and multiply strings.


def multiply(p1,p2):
    return p1*p2
print(multiply(4,5))
print(multiply('a',5))
print(multiply(5,'a'))