# keep asking the user for input until they enter a number between 1 and 10



for _ in range(100):  # arbitrary big number of attempts
    number = int(input("Input a number between 1 and 10: "))
    if 1 <= number <= 10:
        print(f"Thank you! You entered {number}.")
        break
    else:
        print("Invalid input. Try again.")


       