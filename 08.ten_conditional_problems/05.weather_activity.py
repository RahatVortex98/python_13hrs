# Suggest an activity based on the weather(e.g: Sunny-Go for walk,Rainy-Read a book,snowy-Build a snowman)

weather = input("What's the weather? : ")

if weather.lower() == 'sunny':
    print('Go for walk')
elif weather.lower() == 'rainy':
    print('Read a book')
elif weather.lower() == 'snowy':
    print('Build a Snowman')
else:
    print("Hmm... I don't have an activity suggestion for that weather.")