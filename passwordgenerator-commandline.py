import random
import os
import argparse

possibleCharacters = ['a', 'b', 'c', 'd', 'e',
                      'f', 'g', 'h', 'i', 'j',
                      'k', 'l', 'm', 'n', 'o',
                      'p', 'q', 'r', 's', 't',
                      'u', 'v', 'w', 'x', 'y',
                      'z', '1', '2', '3', '4',
                      '5', '6', '7', '8', '9',
                      '0', '!', '@', '#', '$',
                      '%', '^', '&', '*', '?']
password = ""

parser = argparse.ArgumentParser(description="Determines the length of the generated password")
parser.add_argument('Length', metavar='Length', type=int, help="Enter the desired length")
args = parser.parse_args()

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