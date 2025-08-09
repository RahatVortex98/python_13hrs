# Choose a mode based on distance (<3km =walk;3-15 km =bike,>15 =car)


distance =int(input("What's the distance of your destination? :"))



if distance<3:
    print('You should Walk')
elif 3<=distance<=15 :
    print('You can use Bike')
elif distance>15:
    print("You must call a car")
else:
    print("Do whatever u want") 