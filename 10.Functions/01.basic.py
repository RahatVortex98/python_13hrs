def happy_birthday(name,age):
    print(f"Happy birthday to you {name} u are now {age} years old...")

happy_birthday("Bro",20)
happy_birthday('Steve',69)


# name and age is a parameter u can say data
# bro and 20/steve,69 is a argument

# positon of parameters matter

# Return==> statement used to end a function and send a result back to the caller

def add(a,b):
    z=a+b
    print(z)
print(add(1,2))
 

def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first+""+last
full_name = create_name("bro","code")

print(full_name)


# Args and kwargs is a arbitrary 

# *args =allows you to pass multiple non-key arguments
# **kwargs =allows you to pass multiple keyword arguments

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,2,3))


def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value}')

print_address(
            street="123 fake st.",
            apt = "1000",
            city = "mexico",
            state ="Mi",
            zip ="1207"
)


 

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg)
    for value in kwargs.values():
        print(value)


shipping_label("dr","spongebob","sqaurepants",
               
            street="123 fake st.",
            apt = "1000",
            city = "mexico",
            state ="Mi",
            zip ="1207"
               
               
               )