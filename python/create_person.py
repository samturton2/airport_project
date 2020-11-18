import pyodbc
import datetime

class CreatePerson():

    def __init__(self):
        # connect to  DB
        self.server = "ldaijiw-micro.cdix33vx1qyf.eu-west-2.rds.amazonaws.com"
        self.database = "test_database"
        self.username = "ldaijiw"
        self.password = "DreamJLMSU743"

        self.start_connection()

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
            # print(self.cursor.execute("SELECT * FROM test_table;").fetchall())
            return "Connection Successful"

    # TABLES: PASSENGER
    def create_passenger(self, first_name, last_name, dob, gender, passport_number):
        # INPUT: FIRST NAME, LAST NAME, DOB, GENDER, PASSPORT NUMBER
        correct_details = True

        # SQL QUERY TO INPUT INTO PASSENGERS TABLE
        if not passport_number:
            # print("Please enter a passport number")
            correct_details = False
            return "Please enter a passport number"
        elif len(str(passport_number)) > 9:
            # print("Make sure the passport number you have entered is less than 10 characters long")
            correct_details = False
            return "Make sure the passport number you have entered is less than 10 characters long"
        else:
            pass

        if not first_name:
            # print("Please enter a first name")
            correct_details = False
            return "Please enter a first name"
        elif len(first_name) > 32:
            # print("Make sure the first name you have entered is less than 33 characters long")
            correct_details = False
            return "Make sure the first name you have entered is less than 33 characters long"
        else:
            pass

        if not last_name:
            # print("Please enter a last name")
            correct_details = False
            return "Please enter a last name"
        elif len(last_name) > 32:
            # print("Make sure the last name you have entered is less than 33 characters long")
            correct_details = False
            return "Make sure the last name you have entered is less than 33 characters long"
        else:
            pass

        if not dob:
            # print("Please enter a date of birth")
            correct_details = False
            return "Please enter a date of birth"
        else:
            try:
                format_check = datetime.datetime.strptime(dob, '%Y-%m-%d')
            except ValueError:
                # print("Please enter the date of birth in the format: YYYY-MM-DD")
                correct_details = False
                return "Please enter the date of birth in the format: YYYY-MM-DD"

        if not gender:
            # print("Please enter a gender")
            correct_details = False
            return "Please enter a gender"
        elif len(gender) > 16:
            # print("Make sure the gender entered is less than 17 characters long")
            correct_details = False
            return "Make sure the gender entered is less than 17 characters long"
        else:
            pass

        if correct_details == True:
            self.cursor.execute(f"INSERT INTO Passengers (PassportNumber, FirstName, LastName, Gender, DateOfBirth) VALUES ('{passport_number}', '{first_name}', '{last_name}', '{gender}', '{dob}')")
            # OUTPUT: SUCCESSFUL MESSAGE
            # print("Passenger has been successfully added")
            self.db_connection.commit()
            return "Passenger has been successfully added"
        else:
            print("Please try again")
            # return "Please try again"




    # TABLES: STAFF
    def create_staff(self, job_id, first_name, last_name, user_name, pass_word, passport_number, gender, on_location):
        # INPUT: JOB_ID, FIRST NAME, LAST NAME, USERNAME, PASSWORD, PASSPORT NUMBER, GENDER, ON LOCATION
        correct_details = True

        # SQL QUERY TO INPUT INTO STAFF TABLE
        if not job_id:
            # print("Please enter a job ID")
            correct_details = False
            return "Please enter a job ID"
        elif isinstance(job_id, int) == False:
            # print("Please enter the job ID in digits")
            correct_details = False
            return "Please enter the job ID in digits"
        else:
            pass

        if not user_name:
            # print("Please enter a username")
            correct_details = False
            return "Please enter a username"
        elif len(user_name) > 16:
            # print("Make sure the username is less than 17 characters long")
            correct_details = False
            return "Make sure the username is less than 17 characters long"
        else:
            pass


        if not first_name:
            # print("Please enter a first name")
            correct_details = False
            return "Please enter a first name"
        elif len(first_name) > 32:
            # print("Make sure the first name you have entered is less than 33 characters long")
            correct_details = False
            return "Make sure the first name you have entered is less than 33 characters long"
        else:
            pass


        if not last_name:
            # print("Please enter a last name")
            correct_details = False
            return "Please enter a last name"
        elif len(last_name) > 40:
            # print("Make sure the last name you have entered is less than 41 characters long")
            correct_details = False
            return "Make sure the last name you have entered is less than 41 characters long"
        else:
            pass

        if not pass_word:
            # print("Please enter a password")
            correct_details = False
            return "Please enter a password"
        elif len(pass_word) > 32:
            # print("Make sure the password is less than 33 characters long")
            correct_details = False
            return "Make sure the password is less than 33 characters long"
        else:
            pass

        if not passport_number:
            # print("Please enter a passport number")
            correct_details = False
            return "Please enter a passport number"
        elif len(str(passport_number)) > 9:
            # print("Make sure the passport number you have entered in less than 10 characters long")
            correct_details = False
            return "Make sure the passport number you have entered in less than 10 characters long"
        else:
            pass

        if len(str(on_location)) == 0:
            # print("Please confirm is the staff member is on location")
            correct_details = False
            return "Please confirm is the staff member is on location"
        elif (on_location != 0) and (on_location != 1):
            # print("Enter 1 if staff member is on location, enter 0 otherwise")
            correct_details = False
            return "Enter 1 if staff member is on location, enter 0 otherwise"
        else:
            pass

        if not gender:
            # print("Please enter a gender")
            correct_details = False
            return "Please enter a gender"
        elif len(gender) > 16:
            # print("Make sure the gender entered is less than 17 characters long")
            correct_details = False
            return "Make sure the gender entered is less than 17 characters long"
        else:
            pass


        if correct_details == True:
            self.cursor.execute(f"INSERT INTO Staff (Job_id, Username, FirstName, LastName, Gender, UserPassword, PassportNumber, OnLocation) VALUES ({job_id}, '{user_name}', '{first_name}', '{last_name}', '{gender}', '{pass_word}', '{passport_number}', {on_location})")
            # OUTPUT: SUCCESSFUL MESSAGE
            # print("Staff has been successfully added")
            self.db_connection.commit()
            return "Staff member has been successfully added"
        else:
            print("Please try again")
            # return "Please try again"
