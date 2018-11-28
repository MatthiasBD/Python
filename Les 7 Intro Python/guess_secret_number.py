# coding=utf-8

secret = 27

guess = int(raw_input("Guess the secret number:  "))

if secret == guess:
    print "Congratulations you guessed the secret number"
else:
    print "This is not the secret number."
