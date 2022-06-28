import random
import os

possibleCharacters = ['a', 'b', 'c', 'd', 'e',
                      'f', 'g', 'h', 'i', 'j',
                      'k', 'l', 'm', 'n', 'o',
                      'p', 'q', 'r', 's', 't',
                      'u', 'v', 'w', 'x', 'y',
                      'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
specials = ['!', '@', '#', '$', '%', '^', '&', '*', '?']
capitals = []
password = ""

for character in possibleCharacters:
    character = character.upper()
    capitals.append(character)

capitalsEnabled = input("Do you want to enable uppercase letters? [YES] [NO]\n>")
numbersEnabled = input("Do you want to enable numbers? [YES] [NO]\n>")
specialsEnabled = input("Do you want to enable special characters? [YES] [NO]\n>")

while True:
    try:
        passLength = input("How long should the password be?")
        if numbersEnabled.lower() == "yes":
            for number in numbers:
                possibleCharacters.append(number)
        if specialsEnabled.lower() == "yes":
            for special in specials:
                possibleCharacters.append(special)
        if capitalsEnabled.lower() == "yes":
            for capital in capitals:
                possibleCharacters.append(capital)
        passLength = int(passLength)
        generatedPassLength = 0

        while generatedPassLength < passLength:
            character = random.choice(possibleCharacters)
            password = password + character
            generatedPassLength += 1

        os.system("cls")
        print(password)
        input("Press enter to quit...")
        exit()
    except ValueError:
        print("This is not a valid number! Please try again")
