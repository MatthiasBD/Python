from random import randint


def create_lottery_numbers(amount):
    lottery_list = []
    while amount >= (len(lottery_list) + 1):
        number = randint(1, 50)
        if number not in lottery_list:
            lottery_list.append(number)
    return lottery_list


print "Welcome to the Lottery numbers generator."

how_many = raw_input("Please enter how many random numbers you would like to have: ")

while not how_many.isdigit():
    print "This input is not an integer..."
    how_many = raw_input("Please enter how many random numbers you would like to have: ")

how_many = int(how_many)

print create_lottery_numbers(how_many)

print "END"
