# Test file to test functions

from booking_manager import BookingManager
from create_person import CreatePerson
from flight_attendees import FlightAttendees
from flight_trip_manager import FlightTripManager

import unittest
import pytest


# Creating a class to write tests
class Tests(unittest.TestCase):

    # TESTING BOOKING_MANAGER - Leo
    # Creating an object of BookingManager class
    booking = BookingManager()

    def test_make_booking(self):
        pass


    # TESTING CREATE_PERSON - Ubaid
    # Creating an object of CreatePerson class
    person = CreatePerson()

    def test_create_passenger(self):
        pass

    def test_create_staff(self):
        pass



    # TESTING FLIGHT_ATTENDEES - Jared
    # Creating an object of FlightAttendees class
    attendees = FlightAttendees()

    def test_assign_staff_to_flight(self):
        pass

    def test_flight_attendees(self):
        pass


    # TESTING FLIGHT_TRIP_MANAGER - Sam
    # Creating an object of FlightTripManager class
    manage = FlightTripManager()

    def test_create_flight_trip(self):
        pass

    def test_assign_aircraft(self):
        pass

    def test_change_aircraft(self):
        pass



