import os
from database import DBOperations # import the DBOperations class from the database module to perform database operations

# function to delete existing database file if it already exists
def clear_database():
    db_file = "airline.db"
    if os.path.exists(db_file): # check if database file exist 
        os.remove(db_file) # delete if database already exist to prevent overlap
        print("Existing database file removed.")
    else:
        print("No existing database file found.")

# function to insert sample records into database
def insert_sample_data():
    clear_database()
    db = DBOperations() # create an instance to access database methods
    db.create_tables()

    # insert 15 sample destinations where each tuple contains two elements: City and AirportName
    destinations = [
        ("Toronto", "Toronto Pearson Airport"),
        ("Montreal", "Montreal–Trudeau Airport"),
        ("Vancouver", "Vancouver International Airport"),
        ("Calgary", "Calgary International Airport"),
        ("Ottawa", "Ottawa International Airport"),
        ("Edmonton", "Edmonton International Airport"),
        ("Winnipeg", "Winnipeg Richardson Airport"),
        ("Quebec", "Quebec City Jean Lesage Airport"),
        ("Halifax", "Halifax Stanfield International Airport"),
        ("Victoria", "Victoria International Airport"),
        ("Hamilton", "Hamilton International Airport"),
        ("Kitchener", "Waterloo International Airport"),
        ("London", "London International Airport"),
        ("Saskatoon", "Saskatoon International Airport"),
        ("Regina", "Regina International Airport")
    ]
    for city, airport in destinations:
        db.insert_destination(city, airport) # insert each record into the Destination table

    # insert 15 sample pilots using license as the primary key where each tuple contains three elements: License, FirstName, and LastName
    pilots = [
        ("PIL1001", "Moody", "Alam"),
        ("PIL1002", "John", "Benardis"),
        ("PIL1003", "Paola", "Bruscoli"),
        ("PIL1004", "Andrew", "Chinery"),
        ("PIL1005", "Ali", "Cole"),
        ("PIL1006", "Daniela", "De Angeli"),
        ("PIL1007", "Alan", "Hayes"),
        ("PIL1008", "Christina", "Keating"),
        ("PIL1009", "Zack", "Lyons"),
        ("PIL1010", "Phillipa", "Owen"),
        ("PIL1011", "Bhagyashree", "Patil"),
        ("PIL1012", "Sophie", "Pawson"),
        ("PIL1013", "Benjamin", "Ralph"),
        ("PIL1014", "Hardeep", "Sidhu"),
        ("PIL1015", "Michael", "Wright")
    ]
    for license, first_name, last_name in pilots:
        db.insert_pilot(license, first_name, last_name) # insert each record into the Pilot table

    # insert 15 sample flights where each tuple contains the following elements: FlightOrigin, FlightDestination, DepartureDate, Status, PilotID
    flights = [
        (1, 2, "2025-03-01", "Scheduled", "PIL1001"),
        (2, 3, "2025-03-02", "Delayed", "PIL1002"),
        (3, 4, "2025-03-03", "Scheduled", "PIL1003"),
        (4, 5, "2025-03-04", "Cancelled", "PIL1004"),
        (5, 6, "2025-03-05", "Scheduled", "PIL1005"),
        (6, 7, "2025-03-06", "Scheduled", "PIL1006"),
        (7, 8, "2025-03-07", "Scheduled", "PIL1007"),
        (8, 9, "2025-03-08", "Scheduled", "PIL1008"),
        (9, 10, "2025-03-09", "Scheduled", "PIL1009"),
        (10, 11, "2025-03-10", "Scheduled", "PIL1010"),
        (11, 12, "2025-03-11", "Delayed", "PIL1011"),
        (12, 13, "2025-03-12", "Scheduled", "PIL1012"),
        (13, 14, "2025-03-13", "Scheduled", "PIL1013"),
        (14, 15, "2025-03-14", "Scheduled", "PIL1014"),
        (15, 1, "2025-03-15", "Scheduled", "PIL1015")
    ]
    for origin, destination, date, status, pilot in flights:
        db.insert_flight(origin, destination, date, status, pilot) # insert each record into the Flight table

    print("Sample data inserted successfully.")

if __name__ == "__main__":
    insert_sample_data()