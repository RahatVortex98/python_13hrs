# A prime number is a whole number greater than 1 that has only two factors (or divisors): 1 and the number itself. In simpler terms, it's a number that can only be divided evenly by 1 and itself. For example, 2, 3, 5, 7, 11, and 13 are prime numbers. 




number = 29
is_prime = True

if number>1:
    for i in range(2,number):
        if(number % i)==0:
            is_prime=False
            break
print(is_prime)
         