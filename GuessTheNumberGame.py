# This is a guess the number Game

import random

print("Hello What is your Name")
name = input()

print("Well " + name + " I'm thinking a number between 1 and 20..")
secreteNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print("Take a Guess..Please")
    guess = int(input())

    if guess < secreteNumber:
        print("Your guess is too low")
    elif guess > secreteNumber:
        print("Your guess is too High.")
    else:
        break   # This condition is for the correct guess
if guess == secreteNumber:
    print("Good job " + name + " ! You guess my number in " + str(guessesTaken) + " guesses.")
else:
    print("Nope. The number I was thinking of was " + str(secreteNumber))

print("You took " + str(guessesTaken) + " Guesses.")
