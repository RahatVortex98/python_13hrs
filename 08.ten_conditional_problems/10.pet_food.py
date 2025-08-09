# Pet food based on the pet's species and age (DOG,<2years-puupy food,Cat:>5 years-Senior cat food)


pet=input("what's your pet type (Dog/Cat) : ")
age =int(input('Age?  '))

if pet.lower()=='dog' and age<2:
    print('You need puppy food for your ',pet)
elif pet.lower()=='cat' and age>5:

    print('you need Cat food ')
else:
    print("I don't know")