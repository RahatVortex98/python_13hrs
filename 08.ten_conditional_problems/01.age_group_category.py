# AGE GROUP CATEGORIZATION : Classify a person's age group :Child(<13),teenager(13-19),adult(20-59),senior(60+)


age = input("What is your age? : ")

age_count = int(age)

if(age_count<13):
    print("Child")
elif(age_count<=13 or age_count<=19):
    print("Teen")
elif(age_count<=20 or age_count<=59):
    print("Adult")
else:
    print("Senior")