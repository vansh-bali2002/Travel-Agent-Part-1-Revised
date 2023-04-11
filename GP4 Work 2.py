import random

# 1. Display the welcome message
def welcome():
    print('''
Welcome ! I am your friendly travel agent bot.
I will ask you some questions , and make a
recommendation based on your answer .
If you are interested , I will provide you
with a one -time password to create a user
account on our website 
''')

# 2. Prompt for the users name
def ask_userinformation():
    name = input("What is your name? --> ")
    print("Hello dear " + name + " ! \n")

    # 3. Prompt for the users age.

    age = askNumber("What is your age? --> ")

    if age > 64:
        print("Great ! We offer a senior discount ." + "\n" + "For every year over 64 , you get 1% off ." + "\n")
        discount=age-64
    else:
        print()
        discount=0

    # 4. Prompt for number of nights the user wants to stay.

    nights = int(input('For how many nights do you want to stay? --> '))
    return name,age,nights

def ask_yesno(question):
    response = input(question + " (y/n) ")
    if response=="y":
        return True
    else:
        return False

def ask_userpreferences():
    # 5. Ask user if they like cultural and classical music.

    music = ask_yesno("Do you like cultural and classical music?")

# 6. Ask user if they like beaches and surfing.

    beach = ask_yesno('Do you like beaches and surfing?')
    return music,beach

def askNumber(question):
    number=int(input(question))
    return number


def discountNumber(age):
    if age > 64:
        discount = age - 64
        return discount
    else:
        return 0


def totalCosts(flightPrice, hotelPrice, nights, age):
    if age > 64:
        discount = age - 64
        return (flightPrice + (hotelPrice * nights)) * (1.0 - int(discount) / 100)
    else:
        return (flightPrice + (hotelPrice * nights))


def tripDetails(destination,flightPrice,hotelPrice,nights, age):
    if destination == "Bali":
        print('')
        print("How about a trip to Bali?")
        print("Flight: 849.93$")
        print("Hotel: 235.35$/night")
        print(totalCosts(flightPrice, hotelPrice, nights, age))
    elif destination == "Vienna":
        print('')
        print("How about a trip to Vienna?")
        print("Flight: 997.93$")
        print("Hotel: 143.84$/night")
        print(totalCosts(flightPrice, hotelPrice, nights, age))

def suggestTrip(music, beach, viennaPrice, baliPrice):
    if bool(music) == True:
        if bool(beach) == True:
            return 'Bali'

        if bool(beach) == False:
            return 'Vienna'
    if bool(music) == False:
        if bool(beach) == True:
            return 'Bali'
        if bool(beach) == False:
            return None
def createAccount():

    answer = ask_yesno("Do you want to create an account")

    if answer == True:

        password_first_character = str(name[0])

        # This will select the last character
        password_last_character = str(name[-1])

        # The variable will save the remainder of the age divided by 8
        n = age % 8

        # Create a variable and set it to the formula of the password.
        password = password_last_character * int(n) + password_first_character + (random.randint(0, 5) * "!")
        print("Looking forward to working with you! ")
        print("Your one time password is: ",password)
        print("Goodbye.")
    else:
        print("Sorry to hear that . Please consider using our service again .")

# Running all the functions

def Flight_Bot():

    welcome()
    name,age,nights=ask_userinformation()
    discount = discountNumber(age)
    flight_vienna = 997.93
    flight_bali = 849.93
    hotel_vienna = 143.84
    hotel_bali = 235.35
    viennaPrice = (flight_vienna + hotel_vienna * nights)*discount
    baliPrice = (flight_bali + hotel_bali * nights)*discount
    music,beach=ask_userpreferences()
    destination=suggestTrip(music,beach,baliPrice,viennaPrice)
    if destination=="Bali":
        flightPrice=flight_bali
        hotelPrice=hotel_bali
    elif destination=="Vienna":
        flightPrice=flight_vienna
        hotelPrice=hotel_vienna
    print(tripDetails(destination,flightPrice,hotelPrice,nights,age))
    createAccount()

Flight_Bot()