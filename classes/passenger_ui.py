import pyodbc
import pandas as pd
from tabulate import tabulate

class Passenger:
    def __init__(self):
        import pyodbc
        import pandas as pd
        from tabulate import tabulate
        
        # Connecting to  DB
        self.server = "ldaijiw-micro.cdix33vx1qyf.eu-west-2.rds.amazonaws.com"
        self.database = "test_database"
        self.username = "ldaijiw"
        self.password = "DreamJLMSU743"

        # Runs the connection method to connect to server
        self.start_connection()

        # Immediately initialise the passenger_ui
        self.passenger_ui()

    def start_connection(self):
        # Server name, DB name, username, and password are required to connect with pyodbc
        try:
            self.db_connection = pyodbc.connect(
                f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}")

            self.cursor = self.db_connection.cursor()
        except (ConnectionError, pyodbc.OperationalError, pyodbc.DatabaseError):
            return "Connection Unsuccessful"

        else:
            # print(self.cursor.execute("SELECT * FROM test_table;").fetchall())
            return "Connection Successful"

    # If user selects passenger in the loging screen, this method is run
    def passenger_ui(self):
        print("""
        
        Welcome to London Heathrow Airport!
        AVAILABLE OPTIONS
        
        1. View your Ticket Details
        2. View current flights
        
        """)
        user_input = int(input("What would you like to do?\n -> "))

        # If passenger wants to see their ticket details, ask for ticket id and outputs the ticket info
        if user_input == 1:
            user_ticket_id = int(input("What is your Ticket ID?\n -> "))
            your_ticket_query = f"""
            SELECT
                TicketDetails.Ticket_id,
                Passengers.FirstName + ' ' + Passengers.LastName AS "Name",
                TicketDetails.FlightTrip_id,
                FlightTrip.ArrivalAirport,
                Airports.AirportCountry,
                FlightTrip.DepartureTime,
                FlightTrip.TicketPrice
            FROM TicketDetails
            INNER JOIN Passengers ON TicketDetails.Passenger_id = Passengers.Passenger_id
            INNER JOIN FlightTrip ON TicketDetails.FlightTrip_id = FlightTrip.FlightTrip_id
            INNER JOIN Airports ON FlightTrip.DepartureAirport = Airports.Airport_id
            WHERE TicketDetails.Ticket_id = {user_ticket_id}
            """
        #see ticket_id, firstname, lastname, flighttrip id, arrivalairport, departuretime, ticket price

            # Uses pandas to output ticket details
            ticket_details = pd.read_sql_query(f"{your_ticket_query}", self.db_connection)
            df1 = pd.DataFrame(ticket_details)
            print(tabulate(df1, headers = [' ', 'Ticket ID', 'Name', 'Flight Trip ID', 'Arrival Airport', 'Country', 'Departure Date & Time', 'Ticket Price (£)'], tablefmt='psql'))

        # If passenger wants to see current flights, run this method
        if user_input == 2:
            current_flights_query = """
            SELECT 
                FlightTrip.DepartureTime,
                FlightTrip.FlightTrip_id,
                FlightTrip.ArrivalAirport,
                Airports.AirportCountry
            FROM FlightTrip
            INNER JOIN Airports ON FlightTrip.DepartureAirport = Airports.Airport_id
            ORDER BY FlightTrip.DepartureTime
            """
        # See departure time, flighttrip id, Arrival airport, arrival country

            # Outputs all of the current flights in the terminal
            current_flights = pd.read_sql_query(f"{current_flights_query}", self.db_connection)
            df2 = pd.DataFrame(current_flights)
            print(tabulate(df2, headers = ['', 'Departure Date & Time', 'Flight Trip ID', 'Arrival Airport', 'Country'], tablefmt = 'psql'))


# To run the class
# def main():
#
#     test = Passenger()
#
#
# if __name__ == '__main__':
#     main()
