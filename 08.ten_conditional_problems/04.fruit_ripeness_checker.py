# Determine if a fruit is ripe,overripe,or unripe based on it's color(e.g.Banana green-unripe,yellow-Ripe,Brown-overripe)

color=input("what's the color of that fruits? : ")
fruit=input("Name of the fruits? :")



if color.lower() =='green':
    print(f'This {fruit} is Unripe')
elif color.lower() =='yellow':
    print(f'This {fruit} is Ripe')
elif color.lower()== 'Brown':
    print(f'This {fruit}is Overripe')

else:
    print(f"I didn't get that {color} of {fruit} in my data base")