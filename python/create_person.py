import pyodbc
import datetime

class CreatePerson():

    def __init__(self):
        # the following block of code is used to establish a pyodbc connection to northwind database
        self.server = "databases1.spartaglobal.academy"
        self.database = "Northwind"
        self.username = "SA"
        self.password = "Passw0rd2018"
        self.northwind_connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.northwind_connection.cursor()

    # TABLES: PASSENGER
    def create_passenger(self, first_name, last_name, dob, passport_number):
        # INPUT: FIRST NAME, LAST NAME, DOB, PASSPORT NUMBER
        correct_details = True

        # SQL QUERY TO INPUT INTO PASSENGERS TABLE
        if not passport_number:
            print("Please enter a passport number")
            correct_details = False
        elif len(passport_number) > 9:
            print("Make sure the passport number you have entered in less than 10 characters long")
            correct_details = False
        else:
            pass

        if not first_name:
            print("Please enter a first name")
            correct_details = False
        elif len(first_name) > 32:
            print("Make sure the first name you have entered is less than 33 characters long")
            correct_details = False
        else:
            pass

        if not last_name:
            print("Please enter a last name")
            correct_details = False
        elif len(last_name) > 32:
            print("Make sure the last name you have entered is less than 33 characters long")
            correct_details = False
        else:
            pass

        if not dob:
            print("Please enter a date of birth")
            correct_details = False
        else:
            try:
                format_check = datetime.datetime.strptime(dob, '%Y-%m-%d')
                self.cursor.execute(f"INSERT INTO Passengers (DateOfBirth) VALUES ('{dob}')")
            except ValueError:
                print("Please enter the date of birth in the format: YYY-MM-DD")
                correct_details = False

        if correct_details == True:
            self.cursor.execute(f"INSERT INTO Passengers (PassportNumber, FirstName, LastName, DateOfBirth) VALUES ('{passport_number}', '{first_name}', '{last_name}', {dob})")
            # OUTPUT: SUCCESSFUL MESSAGE
            print("Passenger has been successfully added")
        else:
            print("Incorrect Details. Please make sure you have entered your details correctly")




    # TABLES: STAFF
    def create_staff(self, first_name, last_name, user_name, pass_word, passport_number, on_location):
        # INPUT: FIRST NAME, LAST NAME, USERNAME, PASSWORD, PASSPORT NUMBER, ON LOCATION
        correct_details = True

        # SQL QUERY TO INPUT INTO STAFF TABLE
        if not user_name:
            print("Please enter a username")
            correct_details = False
        elif len(passport_number) > 16:
            print("Make sure the username is less than 17 characters long")
            correct_details = False
        else:
            pass


        if not first_name:
            print("Please enter a first name")
            correct_details = False
        elif len(passport_number) > 32:
            print("Make sure the first name you have entered is less than 33 characters long")
            correct_details = False
        else:
            pass


        if not last_name:
            print("Please enter a last name")
            correct_details = False
        elif len(passport_number) > 40:
            print("Make sure the first name you have entered is less than 41 characters long")
            correct_details = False
        else:
            pass

        if not pass_word:
            print("Please enter a password")
            correct_details = False
        elif len(pass_word) > 32:
            print("Make sure the password is less than 33 characters long")
            correct_details = False
        else:
            pass

        if not passport_number:
            print("Please enter a passport number")
            correct_details = False
        elif len(passport_number) > 9:
            print("Make sure the passport number you have entered in less than 10 characters long")
            correct_details = False
        else:
            pass

        if not on_location:
            print("Please confirm is the staff member is on location")
            correct_details = False
        elif (on_location != 0) and (on_location != 1):
            print("Enter 1 if staff member is on location, enter 0 otherwise")
            correct_details = False
        else:
            pass


        if correct_details == True:
            self.cursor.execute(f"INSERT INTO Staff (Username, FirstName, LastName, UserPassword, PassportNumber, OnLocation) VALUES ('{user_name}', '{first_name}', '{last_name}', '{pass_word}', '{passport_number}', {on_location})")
            # OUTPUT: SUCCESSFUL MESSAGE
            print("Staff has been successfully added")
        else:
            print("Incorrect Details. Please make sure you have entered your details correctly")


