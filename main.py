from database import DBOperations # import the DBOperations class from database module

def main():
    db = DBOperations() # create an instance of DBOperations to interact with the SQLite database

    # display the menu and process user input
    while True:
        print("Main Menu:")
        print("1. Add a New Flight")
        print("2. View Flights by Criteria")
        print("3. Update Flight Information")
        print("4. Assign Pilot to Flight")
        print("5. View Pilot Schedule")
        print("6. View/Update Destination Information")
        print("7. Flight Summary")
        print("8. Exit")
        choice = input("Enter your choice: ")

        # user selects option 1: Add a New Flight
        if choice == "1":
            try:
                origin = int(input("Enter origin DestinationID: "))
                destination = int(input("Enter destination DestinationID: "))
            except ValueError:
                print("Please enter numeric values for DestinationID.")
                continue
            date = input("Enter departure date (YYYY-MM-DD): ")
            print("Select flight status:")
            print("1. Scheduled")
            print("2. Delayed")
            print("3. Cancelled")
            choice_status = input("Enter your choice (default 1): ") or "1"
            # map the user's selection to the status string
            if choice_status == "1":
                status = "Scheduled"
            elif choice_status == "2":
                status = "Delayed"
            elif choice_status == "3":
                status = "Cancelled"
            else:
                print("Invalid selection.") # invalid input defaults to 'Scheduled' status
                status = "Scheduled"
            db.insert_flight(origin, destination, date, status)
            print("New flight added.")

        # user selects option 2: View Flights by Criteria
        elif choice == "2":
            print("Search by criteria:")
            print("a. FlightDestination")
            print("b. Status")
            print("c. DepartureDate")
            print("d. View All Flights")
            crit = input("Enter criteria (a/b/c/d): ").lower()
            if crit == "a":
                criteria = "FlightDestination"
                try:
                    value = int(input("Enter DestinationID for destination: "))
                except ValueError:
                    print("Please enter a numeric DestinationID.")
                    continue
                db.view_flights_by_criteria(criteria, value)
            elif crit == "b":
                criteria = "Status"
                value = input("Enter flight status: ")
                db.view_flights_by_criteria(criteria, value)
            elif crit == "c":
                criteria = "DepartureDate"
                value = input("Enter departure date (YYYY-MM-DD): ")
                db.view_flights_by_criteria(criteria, value)
            elif crit == "d":
                # view all flights without filtering
                db.view_all_flights()
            else:
                print("Invalid criteria selected.")

        # user selects option 3: Update Flight Information
        elif choice == "3":
            try:
                flight_id = int(input("Enter FlightID to update: "))
            except ValueError:
                print("Please enter a numeric FlightID.")
                continue
            print("Update options:")
            print("1. DepartureDate")
            print("2. Status")
            option = input("Enter your update choice: ")
            if option == "1":
                new_date = input("Enter new departure date (YYYY-MM-DD): ")
                db.update_flight(flight_id, "DepartureDate", new_date)
            elif option == "2":
                print("Select new flight status:")
                print("1. Scheduled")
                print("2. Delayed")
                print("3. Cancelled")
                choice_status = input("Enter your choice (default 1): ") or "1"
                if choice_status == "1":
                    new_status = "Scheduled"
                elif choice_status == "2":
                    new_status = "Delayed"
                elif choice_status == "3":
                    new_status = "Cancelled"
                else:
                    print("Invalid selection, defaulting to Scheduled.")
                    new_status = "Scheduled"
                db.update_flight(flight_id, "Status", new_status)
            else:
                print("Invalid update option.")

        # user selects option 4: Assign Pilot to Flight
        elif choice == "4":
            try:
                flight_id = int(input("Enter FlightID to assign pilot: "))
            except ValueError:
                print("Please enter a numeric FlightID.")
                continue
            pilot_id = input("Enter Pilot License (e.g., PIL1001): ")
            db.assign_pilot_to_flight(flight_id, pilot_id)

        # user selects option 5: View Pilot Schedule
        elif choice == "5":
            pilot_id = input("Enter Pilot License to view schedule (e.g., PIL1001): ")
            db.view_pilot_schedule(pilot_id)

        # user selects option 6: View/Update Destination Information
        elif choice == "6":
            print("Destination Information: (All Destinations)")
            db.view_destinations()
            update_prompt = input("Do you want to update any destination? (y/n): ")
            if update_prompt.lower() == 'y':
                try:
                    dest_id = int(input("Enter DestinationID to update: "))
                except ValueError:
                    print("Please enter a numeric DestinationID.")
                    continue
                new_city = input("Enter new city (this will automatically update the airport name): ")
                # define the mapping from allowed Canadian cities to their default airport names
                city_to_airport = {
                    "Toronto": "Toronto Pearson Airport",
                    "Montreal": "Montréal–Trudeau Airport",
                    "Vancouver": "Vancouver International Airport",
                    "Calgary": "Calgary International Airport",
                    "Ottawa": "Ottawa Macdonald–Cartier Airport",
                    "Edmonton": "Edmonton International Airport",
                    "Winnipeg": "Winnipeg Richardson Airport",
                    "Quebec City": "Quebec City Jean Lesage Airport",
                    "Halifax": "Halifax Stanfield Airport",
                    "Victoria": "Victoria International Airport",
                    "Hamilton": "Hamilton International Airport",
                    "Kitchener": "Waterloo International Airport",
                    "London": "London International Airport",
                    "North York": "North York City Centre Airport",
                    "Regina": "Regina International Airport"
                }
                if new_city not in city_to_airport:
                    print("Error: Only allowed Canadian cities are accepted. Allowed cities are:")
                    print(", ".join(city_to_airport.keys()))
                else:
                    db.update_destination(dest_id, "City", new_city)
                    default_airport = city_to_airport[new_city]
                    db.update_destination(dest_id, "AirportName", default_airport)
                    print("Destination updated successfully.")

        elif choice == "7":
            db.summarize_data()

        elif choice == "8":
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()