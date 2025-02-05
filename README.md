# FlightManagement

## Overview
**FlightManagement** is a system designed to handle essential airline operations. It manages flights, destinations, and pilot assignments, providing a command-line interface (CLI) to interact with an SQLite database. Key features include adding and viewing flights, assigning pilots, and summarizing data about flights and pilots.

## Features

### Flight Management
- **Add a New Flight**  
  Enter origin and destination (using DestinationID), a departure date, and a predefined flight status (Scheduled, Delayed, or Cancelled).

- **View Flights by Criteria**  
  Filter flights based on destination, departure date, or status, or view all flights.

- **Update Flight Information**  
  Modify the departure date or status for a specific flight record.

- **Assign Pilot to Flight**  
  Assign or reassign a pilot to a flight.

### Pilot Management
- **View Pilot Schedule**  
  Display all flights assigned to a particular pilot.

### Destination Management
- **View/Update Destination Information**  
  List existing destinations and optionally update a city.

### Data Summaries
- **Summarize Flights**  
  Show how many flights exist for each destination and how many flights each pilot is assigned.

## Setup Instructions

### Prerequisites
- Python 3
- A terminal or IDE (e.g., VS Code) to run Python scripts
