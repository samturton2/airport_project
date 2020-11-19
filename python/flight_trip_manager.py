#import pyodbc
import pyodbc

# import datetime and timedelta
from datetime import datetime, timedelta


class FlightTripManager:
    def __init__(self):
        server = "ldaijiw-micro.cdix33vx1qyf.eu-west-2.rds.amazonaws.com"
        database = "test_database"
        username = "ldaijiw"
        password = "DreamJLMSU743"
        self.db_connection = pyodbc.connect(f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}')
        # create a class variable that's the cursor
        self.cursor = self.db_connection.cursor()


    # TABLES: FLIGHT TRIP, AIRPORTS
    def create_flight_trip(self, DepartureTime, ArrivalAirport, TicketPrice, TicketDiscount):
        # INPUT: DEPARTURE TIME (datetime.today()), ARRIVAL AIRPORT (MAN) , TICKET PRICE (230), TICKET DISCOUNT (0.05)
        # ESTIMATE ARRIVAL TIME (1 hour for now)
        ArrivalTime = DepartureTime + timedelta(hours = 1)
        self.cursor.execute(f"""
        INSERT INTO FlightTrip (DepartureTime, ArrivalTime, DepartureAirport, ArrivalAirport, TicketPrice, TicketDiscount)
        VALUES ('{DepartureTime.strftime('%Y-%m-%d %H:%M:%S')}', '{ArrivalTime.strftime('%Y-%m-%d %H:%M:%S')}', 'LHR', '{ArrivalAirport}', {TicketPrice}, {TicketDiscount});
        """)
        # self.db_connection.commit()
        # Attempt to collect the last inserted flight trip identity
        FlightTrip_id = list(self.cursor.execute(f"SELECT FlightTrip_id FROM FlightTrip WHERE FlightTrip_id = @@IDENTITY;").fetchone())[0]
        # RETURN: FLIGHT TRIP ID
        return FlightTrip_id


    # TABLES: FLIGHT TRIP, AIRCRAFT
    def assign_aircraft(self, FlightTrip_id):
        try:
        # CHECK THAT IT's A VALID FLIGHT TRIP ID
            self.cursor.execute(f"SELECT FlightTrip_id FROM FlightTrip WHERE FlightTrip_id = {FlightTrip_id} ;")
            # SEE IF THERE ARE AIRCRAFTS FREE
            aircrafts_free = list(self.cursor.execute(f"select Aircraft_id FROM Aircraft WHERE AircraftStatus_id = 1;").fetchall())

            if len(aircrafts_free) != 0:
                # FIND FIRST PLANE THAT IS AVAILABLE AND IN CORRECT LOCATION
                Aircraft_id = aircrafts_free[0][0]

                # ASSIGN AIRCRAFT ID TO FLIGHT CHANGE
                self.cursor.execute(f"UPDATE FlightTrip SET Aircraft_id = {Aircraft_id} WHERE FlightTrip_id = {FlightTrip_id};")
                # ASSIGNED TO FLIGHT TO TRUE
                self.cursor.execute(f"UPDATE Aircraft SET AircraftStatus_id = 3 WHERE Aircraft_id = {Aircraft_id};")
                # CHANGE AVAILABLE SEATS TO MAX CAPACITY
                max_capacity = list(self.cursor.execute(f"""
                                SELECT AircraftType.MaxCapacity
                                FROM Aircraft LEFT JOIN AircraftType ON Aircraft.AircraftType_id = AircraftType.AircraftType_id
                                WHERE Aircraft.Aircraft_id = {Aircraft_id};
                                """).fetchone())[0]
                self.cursor.execute(f"UPDATE FlightTrip SET AvailableSeats = {max_capacity} WHERE Aircraft_id = {Aircraft_id};")
                self.db_connection.commit()
                # RETURN: AIRCRAFT ID
                return Aircraft_id
            else:
                return "No Aircraft's are available at this time"
        except:
            return "something went wrong, perhaps incorrect FlightTrip id"

    # TABLES: FLIGHT TRIP, AIRCRAFT
    def change_aircraft(self, FlightTrip_id):
        try:
        # INPUT: FLIGHT TRIP ID
            self.cursor.execute(f"SELECT FlightTrip_id FROM FlightTrip WHERE FlightTrip_id = {FlightTrip_id};")
            # CHECK THAT IT's A VALID FLIGHT TRIP ID
            try:
                # COLLECT CURRENT AIRPLANE ID IF ITS BEEN ASSIGNED AN AIRCRAFT
                Aircraft_id = list(self.cursor.execute(f"SELECT Aircraft_id FROM FlightTrip WHERE FlightTrip_id = {FlightTrip_id};").fetchone())[0]
                # CALL ASSIGN_AIRCRAFT() AGAIN
                newAircraft_id = self.assign_aircraft(FlightTrip_id)

            except:
                # CALL ASSIGN_AIRCRAFT() AGAIN
                newAircraft_id = self.assign_aircraft(FlightTrip_id)
            else:
                self.cursor.execute(f"UPDATE Aircraft SET AircraftStatus_id = 1 WHERE Aircraft_id = {Aircraft_id};")
                self.db_connection.commit()
            finally:
                # RETURN: NEW AIRCRAFT ID
                return newAircraft_id
        except:
            return "something went wrong, perhaps incorrect FlightTrip id"

# if __name__ == '__main__':
#     FTM = FlightTripManager()
#     print(FTM.create_flight_trip(datetime.now(), 'MAN', 230, 5))
#     print(FTM.assign_aircraft(5))
#     print(FTM.change_aircraft(5))