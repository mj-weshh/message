def personalized_message():

    name = input("What's your name: ")
    age = int(input("Enter your age: "))
    location = input("Where do you live? ")

    print(f"Hi {name}, you're {age} and live in {location}.")

personalized_message()