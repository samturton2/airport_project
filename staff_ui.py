import pyodbc
from classes.booking_manager import BookingManager
from classes.flight_trip_manager import FlightTripManager
from classes.database_connector import DBConnector

class StaffUI_1(BookingManager, FlightTripManager):
    def __init__(self):
        # connect to  DB
        self.server = "JaredPC\\JS_1"
        self.database = "Airport"
        self.username = "sa"
        self.password = "passw0rd"
        self.start_connection()

        self.user_options()
        # self.db_connection
        # self.cursor

    def start_connection(self):
        # server name, DB name, username, and password are required to connect with pyodbc
        try:
            self.db_connection = pyodbc.connect(
                f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}"
            )
            self.cursor = self.db_connection.cursor()
        except (ConnectionError, pyodbc.OperationalError, pyodbc.DatabaseError):
            return "Connection Unsuccessful"
        
        else:
            return "Connection Successful"

    # This shows the available options for the staff user
    def user_options(self):
        while True:
            print("""
                Options:
                1. Create a new staff member
                2. Create a new passenger
                3. Create a new flight trip
                4. Assign an aircraft to an existing flight trip
                5. Change the aircraft being used for a flight trip
                6. Check staff availability
                7. Assign staff to a flight
                8. Calculate the income from a flight
                9. Print a list of names of who's on a flight""")
            choice = input("TYPE (X) TO EXIT ---> ").upper().strip()


            if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "X"]:
                continue

            
            # CHECKED
            if choice == "X":
                break


            if choice == "1":
                self.create_new_staff_member()


            if choice == "2":
                pass


            if choice == "3":
                pass


            if choice == "4":
                pass


            if choice == "5":
                pass


            if choice == "6":
                pass


            if choice == "7":
                pass


            if choice == "8":
                pass


            if choice == "9":
                pass


    def create_new_staff_member(self):
        # INPUT: JOB_ID, FIRST NAME, LAST NAME, USERNAME, PASSWORD, PASSPORT NUMBER, GENDER, ON LOCATION
        try:
            job = input("\nWhat's their job? ")
            job = int(job)
        except:
            return print("Please input a number")
        firstname = input("Input first name: ").capitalize().strip()
        lastname = input("Input last name: ").capitalize().strip()
        username = input("Choose a username: ")
        password = input("Create a password: ")
        passportnumber = input("Input the 9-digit Passport number: ")
        gender = input("Input gender: ")
        on_location = 1

        print(self.create_staff(job, firstname, lastname, username, password, passportnumber, gender, on_location))



f = StaffUI_1()
