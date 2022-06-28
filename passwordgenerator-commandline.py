import random
import os
import argparse

parser = argparse.ArgumentParser(description="Determines the length of the generated password")
parser.add_argument('Length', metavar='Length', type=int, help="Enter the desired length")
args = parser.parse_args()

possibleCharacters = ['a', 'b', 'c', 'd', 'e',
                      'f', 'g', 'h', 'i', 'j',
                      'k', 'l', 'm', 'n', 'o',
                      'p', 'q', 'r', 's', 't',
                      'u', 'v', 'w', 'x', 'y',
                      'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
specials = ['!', '@', '#', '$', '%', '^', '&', '*', '?']
password = ""
numbersEnabled = input("Do you want to enable numbers? [YES] [NO]\n>")
specialsEnabled = input("Do you want to enable specials? [YES] [NO]\n>")

if numbersEnabled.lower() == "yes":
    for number in numbers:
        possibleCharacters.append(number)
if specialsEnabled.lower() == "yes":
    for special in specials:
        possibleCharacters.append(special)

try:
    passLength = args.Length
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