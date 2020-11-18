# Test file to test functions

from booking_manager import BookingManager
from create_person import CreatePerson
from flight_attendees import FlightAttendees
from flight_trip_manager import FlightTripManager

import unittest
import pytest
from datetime import datetime

lst = []
for i in range(2, 700, 1):
    lst.append(i)
return lst

# Creating a class to write tests
class Tests(unittest.TestCase):

    # TESTING BOOKING_MANAGER - Leo
    # Creating an object of BookingManager class
    booking = BookingManager()

    def test_start_connection(self):
        self.assertEqual(self.booking.start_connection(), "Connection Successful")

    def test_make_booking(self):
        self.assertEqual(self.booking.make_booking(2, lst), "NOT AVAILABLE")
        self.assertIsInstance(self.booking.make_booking(2, [1, 2, 3]), dict)
        self.assertEqual(self.booking.make_booking('mygoodness', [1, 2, 3]), "INVALID FLIGHT TRIP ID")
        self.assertEqual(self.booking.make_booking(2, 'crazymate'), "INVALID PASSENGER ID")



    # TESTING CREATE_PERSON - Ubaid
    # Creating an object of CreatePerson class
    person = CreatePerson()

    def test_start_connection_persons(self):
        self.assertEqual(self.person.start_connection(), "Connection Successful")

    def test_create_passenger(self):
        self.assertEqual(self.person.create_passenger('matt', 'matttsst', '1996-12-12', 'male', '737272731'), "Passenger has been successfully added")
        self.assertEqual(self.person.create_passenger('matt', 'matttsst', '19961212', 'male', '737272731'), "Please enter the date of birth in the format: YYYY-MM-DD")
        self.assertEqual(self.person.create_passenger('nevergonnagiveyouupnevergonnaletyoudownnevergonnacomearoundandhuryou', 'matttsst', '19961212', 'male', '737272731'), "Make sure the first name you have entered is less than 33 characters long")
        self.assertEqual(self.person.create_passenger('matt', 'matttsst', '1996-12-12', 'ahelicoptertyranassouraserex', '737272731'), "Make sure the gender entered is less than 17 characters long")


    def test_create_staff(self):
        self.assertEqual(self.person.create_staff(2, 'ubaid', 'rockstar', 'yey122', 'yadadad', 632632632, 'male', 0), "Staff has been successfully added")
        self.assertEqual(self.person.create_staff(2, 'ubaid', 'rockstar', 'yey122', 'yadadad', 632632632, 'male', '0'), "Enter 1 if staff member is on location, enter 0 otherwise")
        self.assertEqual(self.person.create_staff(2, 'ubaid', 'rockstar', 'yey122', 'yadadad', 63263263212312323, 'male', 0), "Make sure the passport number you have entered in less than 10 characters long")
        self.assertEqual(self.person.create_staff('two', 'ubaid', 'rockstar', 'yey122', 'yadadad', 632632632, 'male', 0), "Please enter the job ID in digits")




    # TESTING FLIGHT_ATTENDEES - Jared
    # Creating an object of FlightAttendees class

    server = "JaredPC\JS_1"
    database = "Airport"
    username = "sa"
    password = "passw0rd"

    attendees = FlightAttendees(server, database, username, password)

    def test_flight_attendees_list(self):
        self.assertIsInstance(self.attendees.flight_attendees_list(2), tuple)

    def test_check_staff_availability(self):
        self.assertIsInstance(self.attendees.check_staff_availability(), list)

    def test_assign_staff_to_flight(self):
        self.assertIsInstance(self.attendees.assign_staff_to_flight(2, [1, 2, 3]), list)




    # TESTING FLIGHT_TRIP_MANAGER - Sam
    # Creating an object of FlightTripManager class
    manage = FlightTripManager()

    def test_create_flight_trip(self):
        self.assertIsInstance(self.manage.create_flight_trip(datetime.now(), 'CDG', 230, 0.05), int)

    def test_assign_aircraft(self):
        self.assertIsInstance(self.manage.assign_aircraft([23]), int)
        self.assertEqual(self.manage.assign_aircraft([23, 24, 25]), "something went wrong, perhaps incorrect FlightTrip id")
        self.assertEqual(self.manage.assign_aircraft('were not strangers to love, you know the rules and so do i'), "something went wrong, perhaps incorrect FlightTrip id")

    def test_change_aircraft(self):
        self.assertIsInstance(self.manage.assign_aircraft([2]), int)
        self.assertEqual(self.manage.change_aircraft([23, 24, 25]), "something went wrong, perhaps incorrect FlightTrip id")
        self.assertEqual(self.manage.change_aircraft('Yadadadadsilverleague'), "something went wrong, perhaps incorrect FlightTrip id")


#book = BookingManager()

#def test_make_booking(self):
    # self.cursor.execute('''
    # CREATE TABLE [Passengers] (
    # [Passenger_id] INT IDENTITY(1,1) NOT NULL,
    # [PassportNumber] VARCHAR(9) NOT NULL,
    # [FirstName] VARCHAR(32) NOT NULL,
    # [LastName] VARCHAR(32) NOT NULL,
    # [DateOfBirth] DATE NOT NULL,
    # PRIMARY KEY ([Passenger_id])
    # );
    # ''')
    # self.db_connection.commit()

    # table_info = self.cursor.execute('''
    # SELECT
    # TABLE_NAME,
    # COLUMN_NAME
    # FROM INFORMATION_SCHEMA.COLUMNS
    # WHERE TABLE_NAME = 'Passengers';
    # ''').fetchall()
    # print(table_info)

    # insert_data_query = "INSERT INTO Passengers\n(PassportNumber, FirstName, LastName, DateOfBirth)\nVALUES('ABC123456', 'Leo', 'Waltmann', '1999-07-13');"

    # self.cursor.execute(insert_data_query)

    # insert_data_query = "INSERT INTO Passengers\n(PassportNumber, FirstName, LastName, DateOfBirth)\nVALUES('ABC123456', 'Oscar', 'Olive', '2010-01-12');"

    # self.cursor.execute(insert_data_query)

    # insert_data_query = "INSERT INTO Passengers\n(PassportNumber, FirstName, LastName, DateOfBirth)\nVALUES('ABC123456', 'Ben', 'Button', '2019-10-13');"

    # self.cursor.execute(insert_data_query)
    # print(list(self.cursor.execute('''
    # SELECT sp.name, sp.default_database_name
    # FROM sys.server_principals sp
    # WHERE sp.name = SUSER_SNAME();
    # ''')))
    # self.cursor.execute("USE test_db;")
    # print(self.cursor.execute("SELECT * FROM Passengers;").fetchall())
    # self.db_connection.commit()
