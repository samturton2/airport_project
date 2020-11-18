# Test file to test functions

# Importing all of the classes used to create the backend
from booking_manager import BookingManager
from create_person import CreatePerson
from flight_attendees import FlightAttendees
from flight_trip_manager import FlightTripManager

# Importing all of the modules required in the tests
import unittest
import pytest
from datetime import datetime

# The below loop creates a list with 700 passengers to be used in BookingManager test
lst = []
for i in range(2, 420, 1):
    lst.append(i)


# Creating a class to write tests
class Tests(unittest.TestCase):

    # TESTING BOOKING_MANAGER
    # Creating an object of BookingManager class
    booking = BookingManager()

    # Tests that the connection method connects to the Database
    def test_start_connection(self):
        self.assertEqual(self.booking.start_connection(), "Connection Successful")

    # Tests the make_booking method where relevant inputs yield different results
    def test_make_booking(self):
        self.assertEqual(self.booking.make_booking(2, lst), "NOT AVAILABLE")
        self.assertIsInstance(self.booking.make_booking(2, [1, 2, 3]), dict)
        self.assertEqual(self.booking.make_booking('mygoodness', [1, 2, 3]), "INVALID FLIGHT TRIP ID")
        self.assertEqual(self.booking.make_booking(2, 'crazymate'), "INVALID PASSENGER ID")



    # TESTING CREATE_PERSON
    # Creating an object of CreatePerson class
    person = CreatePerson()

    # Tests that the connection method connects to the Database successfully
    def test_start_connection_persons(self):
        self.assertEqual(self.person.start_connection(), "Connection Successful")

    # Tests the create_passenger method with different inputs yielding different results based on the code outputs
    def test_create_passenger(self):
        self.assertEqual(self.person.create_passenger('matt', 'matttsst', '1996-12-12', 'male', '737272731'), "Passenger has been successfully added")
        self.assertEqual(self.person.create_passenger('matt', 'matttsst', '19961212', 'male', '737272731'), "Please enter the date of birth in the format: YYYY-MM-DD")
        self.assertEqual(self.person.create_passenger('nevergonnagiveyouupnevergonnaletyoudownnevergonnacomearoundandhuryou', 'matttsst', '19961212', 'male', '737272731'), "Make sure the first name you have entered is less than 33 characters long")
        self.assertEqual(self.person.create_passenger('matt', 'matttsst', '1996-12-12', 'ahelicoptertyranassouraserex', '737272731'), "Make sure the gender entered is less than 17 characters long")

    # Tests the create_staff method with different inputs yielding different results based on the code outputs
    def test_create_staff(self):
        self.assertEqual(self.person.create_staff(2, 'ubaid', 'rockstar', 'yey122', 'yadadad', 632632632, 'male', 0), "Staff has been successfully added")
        self.assertEqual(self.person.create_staff(2, 'ubaid', 'rockstar', 'yey122', 'yadadad', 632632632, 'male', '0'), "Enter 1 if staff member is on location, enter 0 otherwise")
        self.assertEqual(self.person.create_staff(2, 'ubaid', 'rockstar', 'yey122', 'yadadad', 63263263212312323, 'male', 0), "Make sure the passport number you have entered in less than 10 characters long")
        self.assertEqual(self.person.create_staff('two', 'ubaid', 'rockstar', 'yey122', 'yadadad', 632632632, 'male', 0), "Please enter the job ID in digits")




    # TESTING FLIGHT_ATTENDEES
    # Creating an object of FlightAttendees class

    # Server attributes needed to be specified for the database connection in __init__
    server = "JaredPC\JS_1"
    database = "Airport"
    username = "sa"
    password = "passw0rd"

    attendees = FlightAttendees(server, database, username, password)

    # Tests the flight_attendees_list method to make sure the output is a tuple if inputs are correct
    def test_flight_attendees_list(self):
        self.assertIsInstance(self.attendees.flight_attendees_list(2), tuple)

    # Tests the flight_attendees_list method to make sure the output is a tuple if inputs are correct
    def test_check_staff_availability(self):
        self.assertIsInstance(self.attendees.check_staff_availability(), list)

    # Tests the assign_staff_to_flight method to make sure the correct output is a list if input is correct
    def test_assign_staff_to_flight(self):
        self.assertIsInstance(self.attendees.assign_staff_to_flight(2, [1, 2, 3]), list)




    # TESTING FLIGHT_TRIP_MANAGER
    # Creating an object of FlightTripManager class
    manage = FlightTripManager()

    # Tests the create_flight_trip method to make sure that correct input output an int
    def test_create_flight_trip(self):
        self.assertIsInstance(self.manage.create_flight_trip(datetime.now(), 'MAN', 230, 0.05), int)

    # Tests the assign_aircraft method for various inputs and specifies the correct output
    def test_assign_aircraft(self):
        self.assertIsInstance(self.manage.assign_aircraft(1), int)
        self.assertEqual(self.manage.assign_aircraft([23, 24, 25]), "something went wrong, perhaps incorrect FlightTrip id")
        self.assertEqual(self.manage.assign_aircraft('were not strangers to love, you know the rules and so do i'), "something went wrong, perhaps incorrect FlightTrip id")

    # Tests the change_aircraft method for various inputs and specifies the correct output
    def test_change_aircraft(self):
        self.assertIsInstance(self.manage.assign_aircraft(2), int)
        self.assertEqual(self.manage.change_aircraft([23, 24, 25]), "something went wrong, perhaps incorrect FlightTrip id")
        self.assertEqual(self.manage.change_aircraft('Yadadadadsilverleague'), "something went wrong, perhaps incorrect FlightTrip id")
