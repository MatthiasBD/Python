number = raw_input("Select a number between 1 and 100: ")

count = 1

while not number.isdigit() or (int(number) < 1 or int(number) > 100):
    print "This input is incorrect..."
    number = raw_input("Select a number between 1 and 100: ")

number = int(number)

while count <= number:
    if (count % 15) == 0:
        print "fizzbuzz"
    elif (count % 5) == 0:
        print "buzz"
    elif (count % 3) == 0:
        print "fizz"
    else:
        print str(count)
    count += 1
