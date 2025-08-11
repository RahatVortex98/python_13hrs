# create a function that return both area and cir-cumference of a circle  given it's radius

# The Circumference (or) perimeter of circle = 2πR 
# area = πr**2
# pi=3.1416


def circle(r,pi=3.1416):
    area =pi*r**2
    circumference = 2*pi*r
    return area,circumference
a,c =circle(2)
print(f'Area:{a},Circumference:{c}')