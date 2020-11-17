#import pyodbc
import pyodbc

# import datetime and timedelta
from datetime import datetime, timedelta


class FlightTripManager:
    def __init__(self):
        server = "databases1.spartaglobal.academy"
        database = "Group_3_AirportDatabase"
        username = "SA"
        password = "Passw0rd2018"
        self.db_connection = pyodbc.connect(f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}')
        # create a class variable that's the cursor
        self.cursor = self.db_connection.cursor()


    # TABLES: FLIGHT TRIP, AIRPORTS
    def create_flight_trip(self, DepartureTime, ArrivalAirport_id, TicketPrice, TicketDiscount):
        # INPUT: DEPARTURE TIME, DEPARTURE AIRPORT, ARRIVAL AIRPORT, TICKET PRICE, TICKET DISCOUNT
        # ESTIMATE ARRIVAL TIME (1 hour for now)
        ArrivalTime = DepartureTime + timedelta(hours = 1)
        self.cursor.execute(f"""
        INSERT INTO FlightTrip (Aircraft_id, DepartureTime, ArrivalTime, AvailableSeats, DepartureAirport, ArrivalAirport, TicketPrice, TicketDiscount)
        VALUES ( -1, {DepartureTime.strftime('%Y-%m-%d %H:%M:%S')}, {ArrivalTime.strftime('%Y-%m-%d %H:%M:%S')}, -1, '{?? DepartureAirport ??}', '{ArrivalAirport_id}', {TicketPrice}, {TicketDiscount});
        """)
        ## UNFINISHED
        FlightTrip_id = list(self.cursor.execute(f"SELECT FlightTrip_id FROM FlightTrip WHERE {???} ").fetchone())[0]
        # RETURN: FLIGHT TRIP ID
        return FlightTrip_id


    # TABLES: FLIGHT TRIP, AIRCRAFT
    def assign_aircraft(self, FlightTrip_id):
        # INPUT: FLIGHT TRIP ID
        trip_id = self.cursor.execute(f"SELECT FlightTrip_id FROM FlightTrip WHERE FlightTrip_id = {FlightTrip_id} ;")
        # CHECK THAT IT's A VALID FLIGHT TRIP ID
        if len(list(trip_id)) == 1:
            # FIND FIRST PLANE THAT IS AVAILABLE AND IN CORRECT LOCATION
            Aircraft_id = list(self.cursor.execute("SELECT Aircraft_id FROM Aircraft WHERE OnLocation = 1 AND AssignedToFlight = 0;").fetchone())[0]
        try:
            # ASSIGN AIRCRAFT ID TO FLIGHT CHANGE
            self.cursor.execute(f"UPDATE FlightTrip SET Aircraft_id = {Aircraft_id} WHERE FlightTrip_id = {FlightTrip_id};")
            # ASSIGNED TO FLIGHT TO TRUE
            self.cursor.execute(f"UPDATE Aircraft SET AssignedToFlight = 1 WHERE Aircraft_id = {Aircraft_id};")
            # STILL NEED TO CHANGE AVAILABLE SEATS TO MAX CAPACITY
            max_capacity = list(self.cursor.execute(f"""
                            SELECT AircraftType.MaxCapacity
                            FROM Aircraft LEFT JOIN AircraftType ON Aircraft.AircraftType_id = AircraftType.AircraftType_id
                            WHERE Aircraft.Aircraft_id = {Aircraft_id};
                            """).fetchone())[0]
            self.cursor.execute(f"UPDATE FlightTrip SET AvailableSeats = {max_capacity} WHERE Aircraft_id = {Aircraft_id};")
            # RETURN: AIRCRAFT ID
            return int(Aircraft_id)
        except:
            print("something went wrong, perhaps incorrect FlightTrip id, or needs different indexing on SQL lists")

    # # TABLES: FLIGHT TRIP, AIRCRAFT
    # # TABLES: FLIGHT TRIP, AIRCRAFT
    # def change_aircraft(flight_trip_id):
    #     # INPUT: FLIGHT TRIP ID
    #
    #     # REMOVE PLANE ID AND UPDATE PLANE DETAILS TO NO LONGER HAVE DEPARTURE/ARRIVAL INFORMATION
    #
    #     # checks if flight_trip_id passed in by user is in the FlightTrip table
    #     ft_table = self.cursor.execute(f"SELECT * FROM FlightTrip WHERE FlightTrip_id = '{flight_trip_id}'").fetchone()
    #     # if the flight_trip_id is in the table, ft_table will be a list with one item at index 0
    #     if ft_table[0]:  # checks that there is an item in ft_table
    #         self.cursor.execute(
    #             f"UPDATE FlightTrip SET Aircraft_id = NULL, DepartureTime = NULL, ArrivalTime = NULL WHERE FlightTrip_id = '{flight_trip_id}")
    #     else:
    #         print("Please enter a valid flight trip ID")
    #
    #     # CALL ASSIGN_AIRCRAFT() AGAIN
    #     new_aircraft_id = self.assign_aircraft(flight_trip_id)
    #     # NEW PLANE ID = assign_aircraft()
    #
    #     # RETURN: NEW AIRCRAFT ID
    #     return new_aircraft_id
    #
    # def change_aircraft(flight_trip_id):
    #     # INPUT: FLIGHT TRIP ID
    #     # REMOVE PLANE ID AND UPDATE PLANE DETAILS TO NO LONGER HAVE DEPARTURE/ARRIVAL INFORMATION
    #     ft_table = cursor.execute(f"SELECT * FROM FlightTrip WHERE FlightTrip_id = '{flight_trip_id}'").fetchone()
    #     if ft_table[0]:
    #         cursor.execute(
    #             f"UPDATE FlightTrip SET Aircraft_id = NULL, DepartureTime = NULL, ArrivalTime = NULL WHERE FlightTrip_id = '{flight_trip_id}'")
    #     else:
    #         print("Please enter a valid flight trip ID")
    #
    #     # selects all aircrafts that are currently available ie not on flight, not assigned to a flight, and on location
    #     aircraft_table = cursor.execute(
    #         f"SELECT * FROM Aircraft WHERE OnFlight = 0, AssignedToFlight = 0, OnLocation = 1").fetchall()
    #     for row in aircraft_table:
    #         print(row)  # prints all available aircrafts for user to see
    #
    #     # user asked to input the aircraft id of the aircraft they'd like to assign. they'll choose one from the entries printed out above
    #     new_aircraft_id = int(
    #         input("Please enter the aircraft ID of the aircraft you would like to assign to this flight trip: "))
    #
    #     for row in aircraft_table:  # aircraft_table is a list of tuples. for loop iterates over every tuple ie row
    #         if row[0] == new_aircraft_id:  # aircraft_id will is at index 0 of each tuple
    #             # if statement checks if the item at index 0 of one of the tuples in aircraft_table matches the new aircraft id input by the user
    #             cursor.execute(
    #                 f"UPDATE FlightTrip SET Aircraft_id = {new_aircraft_id} WHERE FlightTrip_id = '{flight_trip_id}'")  # sets aircraft id to the new one
    #             return new_aircraft_id
    #         elif row == aircraft_table[
    #             -1]:  # if for loop reaches the last row without having found a match of the new aircraft id input by the user, user is asked to choose an aircraft that's available
    #             print("Please choose an available aircraft")
    #
    # def change_aircraft(flight_trip_id):
    #     # INPUT: FLIGHT TRIP ID
    #     aircraft_table = cursor.execute(
    #         f"SELECT * FROM Aircraft WHERE OnFlight = 0, AssignedToFlight = 0, OnLocation = 1").fetchall()
    #     new_aircraft_id = int(
    #         input("Please enter the aircraft ID of the aircraft you would like to assign to this flight trip: "))
    #     departure_time = ""
    #     arrival_time = ""
    #
    #     # REMOVE PLANE ID AND UPDATE PLANE DETAILS TO NO LONGER HAVE DEPARTURE/ARRIVAL INFORMATION
    #     ft_table = cursor.execute(f"SELECT * FROM FlightTrip WHERE FlightTrip_id = '{flight_trip_id}'").fetchone()
    #     if ft_table[0]:
    #         for row in aircraft_table:
    #             if row[0] == new_aircraft_id:
    #                 cursor.execute(
    #                     f"UPDATE FlightTrip SET Aircraft_id = {new_aircraft_id}, DepartureTime = {departure_time}, ArrivalTime = {arrival_time} WHERE FlightTrip_id = '{flight_trip_id}'")
    #                 return new_aircraft_id
    #             elif row == aircraft_table[-1]:
    #                 print("Please choose an available aircraft")
    #     else:
    #         print("Please enter a valid flight trip ID")
