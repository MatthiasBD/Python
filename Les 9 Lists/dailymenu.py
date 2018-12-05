print "Enter the daily menu."

menu_dict = {}

while True:
    dish = raw_input("Please enter the dish: ")
    price = raw_input("What is the price of the dish: ")
    menu_dict[dish] = price

    new = raw_input("Would you like to enter a new dish? (yes/no) ")

    if new == "no":
        break

with open("menu.txt", "w+") as menu:  # open the TXT file (or create a new one)
    menu.write("Daily menu:\n")  # write into the TXT file
    for item in menu_dict:
        print "- " + item + " -- " + menu_dict[item]
        menu.write("- " + item + " -- " + menu_dict[item] + "\n")  # add task into the TXT file
    menu.write("\n")
