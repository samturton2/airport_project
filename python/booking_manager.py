import pyodbc
from datetime import date

class BookingManager:
    def __init__(self):

        # connect to  DB
        self.server = "databases1.spartaglobal.academy"
        self.database = "Group_3_AirportDatabase"
        self.username = "SA"
        self.password = "Passw0rd2018"

        self.start_connection()


    def start_connection(self):
        # server name, DB name, username, and password are required to connect with pyodbc
        db_connection = pyodbc.connect(
            f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}"
        )
        self.cursor = db_connection.cursor()

    def test(self):
        self.cursor.execute('''
        CREATE TABLE [Passengers] (
        [Passenger_id] INT IDENTITY(1,1) NOT NULL,
        [PassportNumber] VARCHAR(9) NOT NULL,
        [FirstName] VARCHAR(32) NOT NULL,
        [LastName] VARCHAR(32) NOT NULL,
        [DateOfBirth] DATE NOT NULL,
        PRIMARY KEY ([Passenger_id]) 
        );
        ''')

        table_info = self.cursor.execute('''
        SELECT
        TABLE_NAME,
        COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'Passengers';
        ''').fetchall()
        print(table_info)

        insert_data_query = "INSERT INTO Passengers\n(PassportNumber, FirstName, LastName, DateOfBirth)\nVALUES('ABC123456', 'Leo', 'Waltmann', '1999-07-13');"

        self.cursor.execute(insert_data_query)
        


    
    # TABLES: TICKET DETAILS, FLIGHT TRIP, PASSENGERS
    def make_booking(self, flight_trip_id, passenger_id_list):
        # INPUT: FLIGHT TRIP ID, LIST OF PASSENGER ID
        
        # CHECK HOW MANY SEATS THEY WILL NEED (BABY?)
        for passenger_id in passenger_id_list:
            passenger_dob = list(self.cursor.execute(f'''
            SELECT
            DateOfBirth
            FROM Passengers
            WHERE Passenger_id = {passenger_id}
            ''').fetchall()[0])[0]

            passenger_age = date.today() - passenger_dob
        
        print(passenger_dob)
        print(type(passenger_dob))
        print(passenger_age)
        

            
        # CHECK THAT SEATS ARE AVAILABLE
        # IF SEATS ARE NOT AVAILABLE THEN RETURN: NOT AVAILABLE
        # OTHERWISE UPDATE NUMBER OF SEATS AVAILABLE

        # CHECK IF THEY'RE ELIGIBLE FOR DISCOUNT
        
        # FOR EACH PASSENGER
        # ADD FLIGHT TRIP ID/PASSENGER ID TO TICKET DETAILS TABLE
        # ADD COST OF TICKET TO TICKET DETAILS
        
        # RETURN: TICKET ID, COST OF TICKET (ANY DISCOUNT APPLIED), EXTRA FLIGHT DETAILS
        pass

if __name__ == "__main__":
    new_bm = BookingManager()
    new_bm.test()
    new_bm.make_booking(1, [1])