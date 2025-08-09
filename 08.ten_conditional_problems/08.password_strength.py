# Check if a password is  Weak/Medium/Strong. <6(weak),6-10(Medium)and >10(strong)


password=input('Enter Your Password :')


if len(password) <=6:
    print('password is weak')
elif 6<=len(password) <=10:
    print('password is medium')
elif 10<len(password):
    print('password is Strong' )
else:
    print('Write a correct way of password')
