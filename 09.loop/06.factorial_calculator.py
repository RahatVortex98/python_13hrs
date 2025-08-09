# Compute the factorial of a number using loop


# 4!=24

number=int(input("Put a number please: "))

factorial =1 

for i in range(1,number+1):
    factorial *=i
print(f"the factorial of {number} is {factorial} " )