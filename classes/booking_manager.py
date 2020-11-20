import pyodbc
import datetime
from datetime import date
from database_connector import DBConnector
from cryptic import Cryptic

class BookingManager:
    
    # TABLES: TICKET DETAILS, FLIGHT TRIP, PASSENGERS
    # INPUT: FLIGHT TRIP ID, LIST OF PASSENGER ID
    def make_booking(self, flight_trip_id, passenger_id_list):
        # check flight trip id is an int
        if type(flight_trip_id) != int:
            return "INVALID FLIGHT TRIP ID"

        # check passenger id list is a list
        if type(passenger_id_list) != list:
            return "INVALID PASSENGER ID"

        # Check flight_trip_id is valid
        flight_trip_exists = True if self.cursor.execute(f"SELECT COUNT(*) FROM FlightTrip WHERE FlightTrip_id = {flight_trip_id}").fetchone()[0] == 1 else False
        if not flight_trip_exists:
            return "INVALID FLIGHT TRIP ID"

        # Check passenger_id is valid
        for passenger_id in passenger_id_list:
            # Check passenger id is int
            if type(passenger_id) != int:
                return "INVALID PASSENGER ID"
            
            passenger_id_exists = True if self.cursor.execute(f"SELECT COUNT(*) FROM Passengers WHERE Passenger_id = {passenger_id}").fetchone()[0] == 1 else False
            if not passenger_id_exists:
                return "INVALID PASSENGER ID"

        # CHECK HOW MANY SEATS THEY WILL NEED (BABY?)
        passenger_discounts = []
        passengers_need_seat = []
        for passenger_id in passenger_id_list:
            passenger_dob = self.cursor.execute(f'''
            SELECT
            DateOfBirth
            FROM Passengers
            WHERE Passenger_id = {passenger_id}
            ''').fetchone()[0]

            passenger_age = (date.today() - passenger_dob).days // 365

            # CHECK IF THEY'RE ELIGIBLE FOR DISCOUNT
            passenger_discounts.append(1 if passenger_age < 18 else 0)
            # Check if they need a seat
            passengers_need_seat.append(True if passenger_age > 1 else False)

        # Calculate total seats required
        seats_required = sum(passengers_need_seat)
        
        # CHECK THAT SEATS ARE AVAILABLE
        seats_available = self.cursor.execute(f'''
        SELECT AvailableSeats
        FROM FlightTrip
        WHERE FlightTrip_id = {flight_trip_id}
        ''').fetchone()[0]

        # IF SEATS ARE NOT AVAILABLE THEN RETURN: NOT AVAILABLE
        if seats_available < seats_required:
            return "NOT AVAILABLE"
        
        # OTHERWISE UPDATE NUMBER OF SEATS AVAILABLE
        self.cursor.execute(f'''
        UPDATE FlightTrip
        SET AvailableSeats = {seats_available - seats_required}
        WHERE FlightTrip_id = {flight_trip_id}
        ''')
        self.db_connection.commit()
        
        # FOR EACH PASSENGER
        # ADD COST OF TICKET TO TICKET DETAILS
        # retrieve ticket price and ticket discount from flight trip table
        ticket_price = self.cursor.execute(f'''
        SELECT TicketPrice
        FROM FlightTrip
        WHERE FlightTrip_id = {flight_trip_id}
        ''').fetchone()[0]

        ticket_discount = self.cursor.execute(f'''
        SELECT TicketDiscount
        FROM FlightTrip
        WHERE FlightTrip_id = {flight_trip_id}
        ''').fetchone()[0]

        # calculate passenger prices to pay after considering if they're eligible for discount
        passenger_prices = [float(ticket_price) - (float(ticket_price) * float(ticket_discount) * passenger_discount/100) for passenger_discount in passenger_discounts]

        # ADD FLIGHT TRIP ID/PASSENGER ID TO TICKET DETAILS TABLE
        ticket_id_list = []
        for i, passenger_id in enumerate(passenger_id_list):
            self.cursor.execute(f'''
            INSERT INTO TicketDetails (Passenger_id, FlightTrip_id, PricePaid)
            VALUES({passenger_id}, {flight_trip_id}, {passenger_prices[i]})
            ''')
            self.db_connection.commit()

            # retrieve ticket id and append to list
            ticket_id = self.cursor.execute(f'''
            SELECT Ticket_id
            FROM TicketDetails
            WHERE Passenger_id = {passenger_id}
            ''').fetchone()[0]

            ticket_id_list.append(ticket_id)

        # RETURN: TICKET ID, COST OF TICKET (ANY DISCOUNT APPLIED), EXTRA FLIGHT DETAILS
        ticket_info_dict = {ticket_id: passenger_prices[i] for i, ticket_id in enumerate(ticket_id_list)}

        return ticket_info_dict


    # CHECKED LOCALLY
    # The return object is a tuple consisting of Passenger Names and Staff Names in lists
    def flight_attendees_list(self, flight_trip_id):
        passenger_query = f"""
        SELECT Passengers.Passenger_id, Passengers.FirstName, Passengers.LastName, Passengers.PassportNumber
        FROM FlightTrip
        INNER JOIN TicketDetails ON TicketDetails.FlightTrip_id = FlightTrip.FlightTrip_id
        INNER JOIN Passengers ON Passengers.Passenger_id = TicketDetails.Passenger_id
        WHERE FlightTrip.FlightTrip_id = {flight_trip_id};"""
        list_of_passengers = self.cursor.execute(passenger_query)
        retr_passengers = []
        for row in list_of_passengers:
            retr_passengers.append(row)

        staff_query = f"""
        SELECT Staff.Staff_id, Staff.FirstName, Staff.LastName, Staff.PassportNumber
        FROM FlightTrip
        INNER JOIN FlightStaff ON FlightStaff.FlightTrip_id = FlightTrip.FlightTrip_id
        INNER JOIN Staff ON Staff.Staff_id = FlightStaff.Staff_id
        WHERE FlightTrip.FlightTrip_id = {flight_trip_id};"""
        list_of_staff = self.cursor.execute(staff_query)
        retr_staff = []
        for row in list_of_staff:
            retr_staff.append(row)

        return retr_passengers, retr_staff


    # CHECKED LOCALLY
    # Allows use to see the attendee list in terminal
    # This is an extension of flight_attendees_list
    # It takes that return value and prints it
    def print_flight_attendees_list(self, tuple):
        print("\nPassengers:")
        for person in tuple[0]:
            print(person)
        print("\nStaff:")
        for person in tuple[1]:
            print(person)


    # TABLES: PASSENGER
    # Changed due to new ERD diagram -- Wednesday night
    def create_passenger(self, first_name, last_name, dob, gender, passport_number, user_name, pass_word):
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
        else:
            print("Please try again")
            # return "Please try again"
        
        # INPUT USERNAME AND ENCRYPTED PASSWORD INTO PassengerLogins
        crypto = Cryptic()
        encrypted_password = crypto.encrypt(pass_word)

        query = f"INSERT INTO PassengerLogins (PassengerUsername, PassengerPassword) VALUES ('{user_name}', '{encrypted_password}')"
        self.cursor.execute(query)
        self.db_connection.commit()

        return "\nCompleted!"
