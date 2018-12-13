class Vehicle:
    def __init__(self, brand, model, kilometers_done, gen_service_date):
        self.brand = brand
        self.model = model
        self.kilometers_done = kilometers_done
        self.gen_service_date = gen_service_date

    def __str__(self):
        return "Brand & Model: " + self.brand + " " + self.model + \
               "; Kilometers done so far: " + self.kilometers_done + \
               "; General Service Date: " + self.gen_service_date


def list_of_vehicles(vehicles):
    for index, vehicle in enumerate(vehicles):
        print "ID: " + str(index)
        print vehicle

    if not vehicles:
        print "No vehicles in this list of vehicles."


def add_new_vehicle(vehicles):
    brand = raw_input("Give the brand of the vehicle: ")
    model = raw_input("Give the model of the vehicle: ")
    kilometers_done = raw_input("How many kilometers has this vehicle done so far? ")
    gen_service_date = raw_input("Give the general service date: ")

    new_vehicle = Vehicle(brand=brand, model=model, kilometers_done=kilometers_done, gen_service_date=gen_service_date)
    vehicles.append(new_vehicle)

    print ""
    print new_vehicle
    print "This vehicle has been added to the vehicle manager."


def edit_kilometers_done(vehicles):
    print "Select id of the vehicle to change its kilometers done so far:"

    for index, vehicle in enumerate(vehicles):
        print str(index) + ") " + vehicle.brand + " " + vehicle.model

    print ""
    selected_id = raw_input("Of which vehicle do you wish to change the kilometers done so far? (enter ID): ")
    selected_vehicle = vehicles[int(selected_id)]

    new_kilometers_done = raw_input("Please enter a new kilometer done so far for the {} {}: "
                                    .format(selected_vehicle.brand, selected_vehicle.model))
    selected_vehicle.kilometers_done = new_kilometers_done

    print ""
    print "Kilometers done so far updated."


def edit_gen_service_date(vehicles):
    print "Select id of the vehicle to change its general service date:"

    for index, vehicle in enumerate(vehicles):
        print str(index) + ") " + vehicle.brand + " " + vehicle.model

    print ""
    selected_id = raw_input("Of which vehicle do you wish to change the general service date? (enter ID): ")
    selected_vehicle = vehicles[int(selected_id)]

    new_gen_service_date = raw_input("Please enter a new general service date for the {} {}: "
                                     .format(selected_vehicle.brand, selected_vehicle.model))
    selected_vehicle.gen_service_date = new_gen_service_date

    print ""
    print "General service date updated."


def main():
    print "Welcome to the vehicle manager"

    alfa_romeo_gtv = Vehicle(brand="Alfa Romeo", model="GTV", kilometers_done="23012", gen_service_date="6/1/2019")
    bmw_x5 = Vehicle(brand="BMW", model="X5", kilometers_done="14506", gen_service_date="7/1/2019")

    vehicles = [alfa_romeo_gtv, bmw_x5]

    while True:
        print ""
        print "Choose one of these options:"
        print "a) See all your vehicles"
        print "b) Add a new vehicle"
        print "c) Edit the kilometers done so far"
        print "d) Edit the general service date"
        print "e) Quit the program."
        print ""

        selection = raw_input("Enter your selection (a, b, c, d or e): ")

        if selection.lower() == "a":
            list_of_vehicles(vehicles)
        elif selection.lower() == "b":
            add_new_vehicle(vehicles)
        elif selection.lower() == "c":
            edit_kilometers_done(vehicles)
        elif selection.lower() == "d":
            edit_gen_service_date(vehicles)
        elif selection.lower() == "e":
            print "Thanks for using the program. Bye!"
            break
        else:
            print "I do not understand your choice. Try again."
            continue

    with open("VehicleManager.txt", "w+") as vehicle_manager:  # open the TXT file (or create a new one)
        vehicle_manager.write("Vehicles in the program:\n")  # write into the TXT file
        for vehicle in vehicles:
            vehicle_manager.write("Brand & Model: " + vehicle.brand + " " + vehicle.model +
                                  "; Kilometers done so far: " + vehicle.kilometers_done +
                                  "; General Service Date: " + vehicle.gen_service_date + "\n")


if __name__ == '__main__':
    main()
