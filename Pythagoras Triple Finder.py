# This is a Pythagoras Triple finder - enter the start and end range and let it do its' thing!
# Coded by Max Offer - 05/11/2025
# This code involved a use of AI which helped explain certain code is pseudocode - IT WAS NOT WRITTEN BY AI!
from time import sleep

startDigitInputRaw = input("ENTER MIN DIGIT\n")
endDigitInputRaw = input("ENTER MAX DIGIT\n")

print("PYTHAGOREAN TRIPLES COMING UP:")
sleep(1)

startDigit = int(startDigitInputRaw)
endDigit = int(endDigitInputRaw)

def triplefinder():

    for a2 in range(startDigit+1, endDigit+1):
        for b2 in range(a2, endDigit+1):
            for c2 in range(b2, endDigit+1):

                if (a2*a2 + b2*b2 == c2*c2):
                        print(a2, b2, c2)


triplefinder()