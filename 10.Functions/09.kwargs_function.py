# Create a function that accepts any number of keyword arguments and prints them in the format key:value



def super_hero(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")


super_hero(name='Iron Man',power='Ai')
super_hero(name='Hulk',power='smash')
super_hero(name='Captain America',power='Sheild',nation="america")