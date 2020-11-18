from accounting import Accounting

import unittest
import pytest

class TestAccounting(unittest.TestCase):

    accounting = Accounting()

    def test_start_connection(self):
        self.assertEqual(self.accounting.start_connection(), "Connection Successful")

    def test_calculate_income(self):
        self.assertEqual(self.accounting.calculate_ticket_income(2), "The total income from ticket sales for flight 2 is: £1180.00")