import pyodbc
from os import system, name
import pandas as pd
from tabulate import tabulate
from database_connector import DBConnector
import time

def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system("clear")

class Passenger(DBConnector):
    def __init__(self):
        super().__init__()
        # Immediately initialise the passenger_ui
        self.passenger_ui()


    # If user selects passenger in the login screen, this method is run
    def passenger_ui(self):
        print('Welcome to London Heathrow Airport!')
        while True:
            clear()
            print("""
            AVAILABLE OPTIONS
            
            1. View your Ticket Details
            2. View current flights
            3. Logout
            TYPE <X> TO EXIT
            """)
            user_input = input("What would you like to do?\n -> ").strip().upper()
            if user_input not in ['1', '2', '3', 'X']:
                continue

            if user_input == "X":
                clear()
                exit()

            # If passenger wants to see their ticket details, ask for ticket id and outputs the ticket info
            if user_input == '1':
                clear()
                user_ticket_id = int(input("What is your Ticket ID?\n -> "))
                your_ticket_query = f"""
                SELECT
                    TicketDetails.Ticket_id,
                    Passengers.FirstName + ' ' + Passengers.LastName AS "Name",
                    TicketDetails.FlightTrip_id,
                    FlightTrip.ArrivalAirport,
                    Airports.AirportCountry,
                    FlightTrip.DepartureTime,
                    FlightTrip.TicketPrice,
                    TicketDetails.PricePaid
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
                print('=' * 30)
                print('You ticket details:')
                print('=' * 30)

                print(tabulate(df1, headers = [' ', 'Ticket ID', 'Name', 'Flight Trip ID', 'Arrival Airport', 'Country', 'Departure Date & Time', 'Ticket Price (£)', 'Total Paid (£)'], tablefmt='psql'))
                input("\nPress <ENTER> to continue")
                continue

            # If passenger wants to see current flights, run this method
            if user_input == '2':
                clear()
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
                print('=' * 30)
                print('Current flights')
                print('=' * 30)

                print(tabulate(df2, headers = ['', 'Departure Date & Time', 'Flight Trip ID', 'Arrival Airport', 'Country'], tablefmt = 'psql'))
                input("\nPress <ENTER> to continue")
                continue


            if user_input == '3':
                clear()
                print("Thank you for using the London Heathrow Airport Terminal!")
                return "RETURNED LOGOUT"



# # To run the class
# def main():
#
#     test = Passenger()
#
#
# if __name__ == '__main__':
#      main()
