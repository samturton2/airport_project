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
    def create_flight_trip(self, DepartureTime, ArrivalAirport, TicketPrice, TicketDiscount):
        # INPUT: DEPARTURE TIME (datetime.today()), ARRIVAL AIRPORT (CDG) , TICKET PRICE (230), TICKET DISCOUNT (0.05)
        # ESTIMATE ARRIVAL TIME (1 hour for now)
        ArrivalTime = DepartureTime + timedelta(hours = 1)
        self.cursor.execute(f"""
        INSERT INTO FlightTrip (Aircraft_id, DepartureTime, ArrivalTime, AvailableSeats, DepartureAirport, ArrivalAirport, TicketPrice, TicketDiscount)
        VALUES ( -1, {DepartureTime.strftime('%Y-%m-%d %H:%M:%S')}, {ArrivalTime.strftime('%Y-%m-%d %H:%M:%S')}, -1, 'LHR', '{ArrivalAirport}', {TicketPrice}, {TicketDiscount});
        """)
        # self.db_connection.commit()
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
            Aircraft_id = list(self.cursor.execute("SELECT Aircraft_id FROM Aircraft WHERE AircraftStatus_id = 0;").fetchone())[0]

            # ASSIGN AIRCRAFT ID TO FLIGHT CHANGE
            self.cursor.execute(f"UPDATE FlightTrip SET Aircraft_id = {Aircraft_id} WHERE FlightTrip_id = {FlightTrip_id};")
            # ASSIGNED TO FLIGHT TO TRUE
            self.cursor.execute(f"UPDATE Aircraft SET AircraftStatus_id = 1 WHERE Aircraft_id = {Aircraft_id};")
            # CHANGE AVAILABLE SEATS TO MAX CAPACITY
            max_capacity = list(self.cursor.execute(f"""
                            SELECT AircraftType.MaxCapacity
                            FROM Aircraft LEFT JOIN AircraftType ON Aircraft.AircraftType_id = AircraftType.AircraftType_id
                            WHERE Aircraft.Aircraft_id = {Aircraft_id};
                            """).fetchone())[0]
            self.cursor.execute(f"UPDATE FlightTrip SET AvailableSeats = {max_capacity} WHERE Aircraft_id = {Aircraft_id};")
            # self.db_connection.commit()
            # RETURN: AIRCRAFT ID
            return int(Aircraft_id)
        else:
            return "something went wrong, perhaps incorrect FlightTrip id"

    # TABLES: FLIGHT TRIP, AIRCRAFT
    def change_aircraft(self, FlightTrip_id):
        # INPUT: FLIGHT TRIP ID
        # INPUT: FLIGHT TRIP ID
        trip_id = self.cursor.execute(f"SELECT FlightTrip_id FROM FlightTrip WHERE FlightTrip_id = {FlightTrip_id} ;")
        # CHECK THAT IT's A VALID FLIGHT TRIP ID
        if len(list(trip_id)) == 1:
        try:
            # COLLECT CURRENT AIRPLANE ID IF ITS BEEN ASSIGNED AN AIRPLANE
            Aircraft_id = list(self.cursor.execute("SELECT Aircraft_id FROM FlightTrip_id WHERE AircraftStatus_id = 0;").fetchone())[0]
        Except
        # CALL ASSIGN_AIRCRAFT() AGAIN
        newAircraft_id = self.assign_aircraft(FlightTrip_id)
        # NEW PLANE ID = assign_aircraft()

        # RETURN: NEW AIRCRAFT ID
        return newAircraft_id
