# Movie Ticket are priced based on age :$12 for adults(18 or over),$8 for children,Everyone get a $2 discount on wednesday!





age =int(input("Your age please: "))
day =input("What day today? : ").lower()




if age>=18 :
    price=12
else:
    price=8


if day =='wednesday':
    price=price-2

print(f'Your ticket price is ${price}')