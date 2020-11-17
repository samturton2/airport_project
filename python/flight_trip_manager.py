#import pyodbc
import pyodbc

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
        self.cursor.execute(f"INSERT INTO FlightTrip (Aircraft_id, DepartureTime, ArrivalTime, AvailableSeats, DepartureAirport, ArrivalAirport, TicketPrice, TicketDiscount")
        ## UNFINISHED

        # RETURN: FLIGHT TRIP ID


    # TABLES: FLIGHT TRIP, AIRCRAFT
    def assign_aircraft(self, FlightTrip_id):
        # INPUT: FLIGHT TRIP ID
        trip_id = self.cursor.execute(f"SELECT FlightTrip_id FROM FlightTrip WHERE FlightTrip_id = {FlightTrip_id};")
        # CHECK THAT IT's A VALID FLIGHT TRIP ID
        if len(list(trip_id)) == 1:
            # FIND FIRST PLANE THAT IS AVAILABLE AND IN CORRECT LOCATION
            Aircraft_id = list(self.cursor.execute("SELECT Aircraft_id FROM Aircraft WHERE OnLocation = 1;").fetchone())[0]
        try:
            # ASSIGN AIRCRAFT ID TO FLIGHT CHANGE
            self.cursor.execute(f"UPDATE FlightTrip SET Aircraft_id = {Aircraft_id} WHERE FlightTrip_id = {FlightTrip_id};")
            # ASSIGNED TO FLIGHT TO TRUE
            self.cursor.execute(f"UPDATE Aircraft SET AssignedToFlight = 1 WHERE Aircraft_id = {Aircraft_id};")
            # RETURN: AIRCRAFT ID
            return int(Aircraft_id)

        # STILL NEED TO CHANGE AVAILABLE SEATS TO MAX CAPACITY

        except:
            print("my error message: => incorrect FlightTrip_id")


    # TABLES: FLIGHT TRIP, AIRCRAFT
    def change_aircraft():
        # INPUT: FLIGHT TRIP ID

        # REMOVE PLANE ID AND UPDATE PLANE DETAILS TO NO LONGER HAVE DEPARTURE/ARRIVAL INFORMATION

        # CALL ASSIGN_AIRCRAFT() AGAIN
        # NEW PLANE ID = assign_aircraft()

        # RETURN: NEW AIRCRAFT ID
