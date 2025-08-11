# write a function that greets a user.if no name is provided it should with default name.


def greet(name='Unix'):
    return 'hello there' + name 

print(greet())
print(greet('Linux'))
