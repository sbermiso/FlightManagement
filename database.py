import sqlite3  # import the SQLite module for database operations

# class to encapsulate all database operations
class DBOperations:
    # constructor to initialize the DBOperations instance with a database file name
    def __init__(self, db_name="airline.db"):
        self.db_name = db_name  # set the database file name

    # method to connect to the SQLite database
    def get_connection(self):
        conn = sqlite3.connect(self.db_name) # connect to the SQLite database and allow column access by name
        conn.row_factory = sqlite3.Row
        return conn # return open database connection

    # method to create the necessary tables
    def create_tables(self):
        conn = self.get_connection() # obtain connection to the database
        cursor = conn.cursor() # create cursor for executing SQL commands
        
        # create Destination table for DestinationID, City, and AirportName
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Destination (
                DestinationID INTEGER PRIMARY KEY AUTOINCREMENT,
                City TEXT NOT NULL,
                AirportName TEXT NOT NULL
            )
        """)
        
        # create Pilot table using License as primary key
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Pilot (
                License TEXT PRIMARY KEY,
                FirstName TEXT NOT NULL,
                LastName TEXT NOT NULL
            )
        """)
        
        # create Flight table for FlightID
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Flight (
                FlightID INTEGER PRIMARY KEY AUTOINCREMENT,
                FlightOrigin INTEGER NOT NULL,
                FlightDestination INTEGER NOT NULL,
                DepartureDate TEXT NOT NULL,
                Status TEXT,
                PilotID TEXT,
                FOREIGN KEY (FlightOrigin) REFERENCES Destination(DestinationID),
                FOREIGN KEY (FlightDestination) REFERENCES Destination(DestinationID),
                FOREIGN KEY (PilotID) REFERENCES Pilot(License)
            )
        """)
        
        conn.commit() # commit changes and then close connection
        conn.close()
        print("Tables created successfully.")

    # method to insert a new destination into Destination table
    def insert_destination(self, city, airport_name):
        conn = self.get_connection()
        cursor = conn.cursor()
        # execute query to insert a new destination record with the provided city and airport name
        cursor.execute(
            "INSERT INTO Destination (City, AirportName) VALUES (?, ?)",
            (city, airport_name)
        )
        conn.commit()
        conn.close()

    # method to insert a new pilot into Pilot table
    def insert_pilot(self, license, first_name, last_name):
        conn = self.get_connection()
        cursor = conn.cursor()
        # execute query to insert a new pilot record with the provided license, first name, and last name
        cursor.execute(
            "INSERT INTO Pilot (License, FirstName, LastName) VALUES (?, ?, ?)",
            (license, first_name, last_name)
        )
        conn.commit()
        conn.close()

    # method to insert a new flight into Flight table
    def insert_flight(self, origin, destination, departure_date, status="Scheduled", pilot_id=None):
        conn = self.get_connection()
        cursor = conn.cursor()
        # execute query to insert a new flight record with the provided FlightOrigin, FlightDestination, DepartureDate, Status, and PilotID
        cursor.execute(
            "INSERT INTO Flight (FlightOrigin, FlightDestination, DepartureDate, Status, PilotID) VALUES (?, ?, ?, ?, ?)",
            (origin, destination, departure_date, status, pilot_id)
        )
        conn.commit()
        conn.close()

    # method to retrieve and display all flight records from Flight table
    def view_all_flights(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        # execute query to get all flights
        cursor.execute("SELECT * FROM Flight") 
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(dict(row))
        else:
            print("No flights found.")
        conn.close()

    # method to retrieve and display flights matching specified criteria
    def view_flights_by_criteria(self, criteria, value):
        conn = self.get_connection()
        cursor = conn.cursor()
        # execute query to retrieve all flight records where the column specified by criteria equals the provided value
        query = "SELECT * FROM Flight WHERE " + criteria + " = ?"
        cursor.execute(query, (value,))
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(dict(row))
        else:
            print("No flights found matching the criteria.")
        conn.close()

    # method to update a specific flight record
    def update_flight(self, flight_id, column, new_value):
        conn = self.get_connection()
        cursor = conn.cursor()
        # execute an update query to set the specified column to new_value for the flight with the given FlightID
        query = "UPDATE Flight SET " + column + " = ? WHERE FlightID = ?"
        cursor.execute(query, (new_value, flight_id))
        conn.commit()
        if cursor.rowcount > 0:
            print("Flight updated successfully.")
        else:
            print("Flight not found.")
        conn.close()

    # method to assign a pilot to a flight
    def assign_pilot_to_flight(self, flight_id, pilot_id):
        self.update_flight(flight_id, "PilotID", pilot_id)

    # method to retrieve and display all flights assigned to a specific pilot
    def view_pilot_schedule(self, pilot_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        # execute a query to find flights where PilotID matches the provided pilot_id
        cursor.execute("SELECT * FROM Flight WHERE PilotID = ?", (pilot_id,))
        rows = cursor.fetchall()
        if rows:
            print("Flights for Pilot License", pilot_id)
            for row in rows:
                print(dict(row))
        else:
            print("No flights assigned to this pilot.")
        conn.close()

    # method to retrieve and display all destination records from the Destination table
    def view_destinations(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        # execute a query to get all destinations
        cursor.execute("SELECT * FROM Destination")
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(dict(row))
        else:
            print("No destinations found.")
        conn.close()

    # method to search for a destination by a city name
    def search_destination_by_city(self, city):
        # Search for a destination record where the City column matches (or contains) the given string.
        conn = self.get_connection()
        cursor = conn.cursor()
        # execute a query to find any destination whose City column contains the given string
        cursor.execute("SELECT * FROM Destination WHERE City LIKE ?", ('%' + city + '%',))
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(dict(row))
        else:
            print("No destination found for city:", city)
        conn.close()

    # method to update a destination record
    def update_destination(self, destination_id, column, new_value):
        conn = self.get_connection()
        cursor = conn.cursor()
        # execute an update query to set the specified column to new_value for the destination with the given DestinationID
        query = "UPDATE Destination SET " + column + " = ? WHERE DestinationID = ?"
        cursor.execute(query, (new_value, destination_id))
        conn.commit()
        conn.close()

    # method to summarize the data by executing the selected queries
    def summarize_data(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # query 1: count flights by DestinationID using FlightDestination
        cursor.execute("""
            SELECT FlightDestination, COUNT(*) AS flight_count 
            FROM Flight 
            GROUP BY FlightDestination
        """)
        destination_summary = cursor.fetchall()
        
        # query 2: count flights by pilot using PilotID
        cursor.execute("""
            SELECT PilotID, COUNT(*) AS flight_count 
            FROM Flight 
            WHERE PilotID IS NOT NULL 
            GROUP BY PilotID
        """)
        pilot_summary = cursor.fetchall()
        
        conn.close()
        
        print("Summary: Number of Flights by Destination")
        if destination_summary:
            for row in destination_summary:
                print("DestinationID:", row["FlightDestination"], "->", row["flight_count"], "flights")
        else:
            print("No flight data for destinations.")
        
        print("\nSummary: Number of Flights by Pilot")
        if pilot_summary:
            for row in pilot_summary:
                print("Pilot License:", row["PilotID"], "->", row["flight_count"], "flights")
        else:
            print("No flight data for pilots.")