# print the multiplication table for a given number up to number 10,but skip 5th iteration



number=int(input('Enter a number :'))


for i in range(1,11):
    if i==5:
        continue #skip the iteration


    print(number,'X',i, '=', number*i)