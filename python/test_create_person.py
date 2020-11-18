from create_person import CreatePerson

import unittest
import pytest
from datetime import datetime

class TestCreatePerson(unittest.TestCase):


    person = CreatePerson()

    def test_start_connection_persons(self):
        self.assertEqual(self.person.start_connection(), "Connection Successful")

    def test_create_passenger(self):
        self.assertEqual(self.person.create_passenger('matt', 'matttsst', '1996-12-12', 'male', '737272731'), "Passenger has been successfully added")
        self.assertEqual(self.person.create_passenger('matt', 'matttsst', '19961212', 'male', '737272731'), "Please enter the date of birth in the format: YYYY-MM-DD")
        self.assertEqual(self.person.create_passenger('nevergonnagiveyouupnevergonnaletyoudownnevergonnacomearoundandhuryou', 'matttsst', '19961212', 'male', '737272731'), "Make sure the first name you have entered is less than 33 characters long")
        self.assertEqual(self.person.create_passenger('matt', 'matttsst', '1996-12-12', 'ahelicoptertyranassouraserex', '737272731'), "Make sure the gender entered is less than 17 characters long")

    def test_create_staff(self):
        self.assertEqual(self.person.create_staff(2, 'ubaid', 'rockstar', 'yey122', 'yadadad', 632632632, 'male', 0), "Staff member has been successfully added")
        self.assertEqual(self.person.create_staff(2, 'ubaid', 'rockstar', 'yey122', 'yadadad', 632632632, 'male', '0'), "Enter 1 if staff member is on location, enter 0 otherwise")
        self.assertEqual(self.person.create_staff(2, 'ubaid', 'rockstar', 'yey122', 'yadadad', 63263263212312323, 'male', 0), "Make sure the passport number you have entered in less than 10 characters long")
        self.assertEqual(self.person.create_staff('two', 'ubaid', 'rockstar', 'yey122', 'yadadad', 632632632, 'male', 0), "Please enter the job ID in digits")

