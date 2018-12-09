# coding=utf-8
# This is an import of a particular function of random
from random import randint

# This is an assignment of a random integer between 1 and 100 to the variable secret.
# secret stays the same random input until guessed or the loop stopped
secret = randint(1, 100)

# This is not part of the program, only a check to see what the secret number is.
# print secret


# Implementation of the main function
def main():
    while True:
        new = raw_input("Do you want to guess the secret number between 1 and 100? yes/no ")
        if new.lower() == "no" or new.lower() == "n":
            break

        guessing = raw_input("What is your guess for the secret number: ")

        # this is to check if the input given is correct so the loop can proceed
        # it checks if the guessing number is a digit and between 1 and 100
        while not guessing.isdigit() or (int(guessing) < 1 or int(guessing) > 100):
            print "This input is incorrect..."
            guessing = raw_input("Select a number between 1 and 100: ")
        guessing = int(guessing)

        if guessing == secret:
            print check_guess(guessing)
            break
        else:
            print check_guess(guessing)


# This is the function to check if the guess is correct or not
def check_guess(guess):
    if secret == guess:
        return "Congratulations you guessed the secret number!"
    else:
        return "This is not the secret number."


if __name__ == '__main__':
    main()
