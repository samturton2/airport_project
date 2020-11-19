from database_connector import DBConnector
from datetime import datetime, timedelta

class FlightTripManager(DBConnector):
    
    # TABLES: FLIGHT TRIP, AIRPORTS
    def create_flight_trip(self, DepartureTime, ArrivalAirport, TicketPrice, TicketDiscount):
        # INPUT: DEPARTURE TIME (datetime.today()), ARRIVAL AIRPORT (MAN) , TICKET PRICE (230), TICKET DISCOUNT (0.05)
        # ESTIMATE ARRIVAL TIME (1 hour for now)
        ArrivalTime = DepartureTime + timedelta(hours = 1)
        self.cursor.execute(f"""
        INSERT INTO FlightTrip (DepartureTime, ArrivalTime, DepartureAirport, ArrivalAirport, TicketPrice, TicketDiscount)
        VALUES ('{DepartureTime.strftime('%Y-%m-%d %H:%M:%S')}', '{ArrivalTime.strftime('%Y-%m-%d %H:%M:%S')}', 'LHR', '{ArrivalAirport}', {TicketPrice}, {TicketDiscount});
        """)
        # self.db_connection.commit()
        # Attempt to collect the last inserted flight trip identity
        FlightTrip_id = list(self.cursor.execute(f"SELECT FlightTrip_id FROM FlightTrip WHERE FlightTrip_id = @@IDENTITY;").fetchone())[0]
        # RETURN: FLIGHT TRIP ID
        return FlightTrip_id

    
    # TABLES: FLIGHT TRIP, AIRCRAFT
    def assign_aircraft(self, FlightTrip_id):
        try:
        # INPUT: FLIGHT TRIP ID
            self.cursor.execute(f"SELECT FlightTrip_id FROM FlightTrip WHERE FlightTrip_id = {FlightTrip_id} ;")
            # CHECK THAT IT's A VALID FLIGHT TRIP ID

            # FIND FIRST PLANE THAT IS AVAILABLE AND IN CORRECT LOCATION
            Aircraft_id = list(self.cursor.execute("SELECT Aircraft_id FROM Aircraft WHERE AircraftStatus_id = 1;").fetchone())[0]

            # ASSIGN AIRCRAFT ID TO FLIGHT CHANGE
            self.cursor.execute(f"UPDATE FlightTrip SET Aircraft_id = {Aircraft_id} WHERE FlightTrip_id = {FlightTrip_id};")
            # ASSIGNED TO FLIGHT TO TRUE
            self.cursor.execute(f"UPDATE Aircraft SET AircraftStatus_id = 3 WHERE Aircraft_id = {Aircraft_id};")
            # CHANGE AVAILABLE SEATS TO MAX CAPACITY
            max_capacity = list(self.cursor.execute(f"""
                            SELECT AircraftType.MaxCapacity
                            FROM Aircraft LEFT JOIN AircraftType ON Aircraft.AircraftType_id = AircraftType.AircraftType_id
                            WHERE Aircraft.Aircraft_id = {Aircraft_id};
                            """).fetchone())[0]
            self.cursor.execute(f"UPDATE FlightTrip SET AvailableSeats = {max_capacity} WHERE Aircraft_id = {Aircraft_id};")
            self.db_connection.commit()
            # RETURN: AIRCRAFT ID
            return Aircraft_id
        except:
            return "something went wrong, perhaps incorrect FlightTrip id"


    # TABLES: FLIGHT TRIP, AIRCRAFT
    def change_aircraft(self, FlightTrip_id):
        try:
        # INPUT: FLIGHT TRIP ID
            self.cursor.execute(f"SELECT FlightTrip_id FROM FlightTrip WHERE FlightTrip_id = {FlightTrip_id};")
            # CHECK THAT IT's A VALID FLIGHT TRIP ID
            try:
                # COLLECT CURRENT AIRPLANE ID IF ITS BEEN ASSIGNED AN AIRCRAFT
                Aircraft_id = list(self.cursor.execute(f"SELECT Aircraft_id FROM FlightTrip_id WHERE FlightTrip_id = {FlightTrip_id};").fetchone())[0]
                # CALL ASSIGN_AIRCRAFT() AGAIN
                newAircraft_id = self.assign_aircraft(FlightTrip_id)

            except:
                # CALL ASSIGN_AIRCRAFT() AGAIN
                newAircraft_id = self.assign_aircraft(FlightTrip_id)
            else:
                self.cursor.execute(f"UPDATE Aircraft SET AircraftStatus_id = 1 WHERE Aircraft_id = {Aircraft_id};")
                self.db_connection.commit()
            finally:
                # RETURN: NEW AIRCRAFT ID
                return newAircraft_id
        except:
            return "something went wrong, perhaps incorrect FlightTrip id"


    # CHECKED LOCALLY
    # Checks which staff is available to be assigned to a flight
    # Returns a list of tuples of (Staff_id, FirstName, LastName)
    def check_staff_availability(self):
        query = f"""
        SELECT Staff_id, FirstName, LastName
        FROM Staff
        WHERE OnLocation = 1;
        """

        list_of_available_staff = self.cursor.execute(query)
        retr_staff = []
        for row in list_of_available_staff:
            retr_staff.append(row)

        # If you want to see the list, just print it
        return retr_staff


    
    # TABLES: STAFF
    def create_staff(self, job_id, first_name, last_name, user_name, pass_word, passport_number, gender, on_location, staff_level):
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
            self.cursor.execute(f"INSERT INTO Staff (Job_id, FirstName, LastName, Gender, PassportNumber, OnLocation) VALUES ({job_id}, '{first_name}', '{last_name}', '{gender}', '{passport_number}', {on_location})")
            # OUTPUT: SUCCESSFUL MESSAGE
            # print("Staff has been successfully added")
            self.cursor.execute(f"INSERT INTO StaffLogins (StaffUsername, StaffPassword, StaffLevel) VALUES ('{user_name}', '{pass_word}', {staff_level})")
            self.db_connection.commit()
            return "Staff member has been successfully added"
        else:
            print("Please try again")
            # return "Please try again"

        


    # CHECKED LOCALLY
    # Assign staff to a flight, updates FlightStaff, change corresponding staff OnLocation to 0
    # The list_of_staff should be a list of staff_id as it's the PK
    def assign_staff_to_flight(self, flight_trip_id, list_of_staff_ids):
        # Changes the OnLocation for all the staff in list to 0
        for staff_id in list_of_staff_ids:   
            query_for_onlocation = f"""
            UPDATE Staff
            SET OnLocation = 0
            WHERE Staff_id = {staff_id}
            """
            self.cursor.execute(query_for_onlocation)
            self.db_connection.commit()

        # Adds the flight staff with flight id to the FlightStaff table
        for staff_id in list_of_staff_ids:
            query_for_insertion = f"""
            INSERT INTO FlightStaff (FlightTrip_id, Staff_id)
            VALUES ({flight_trip_id}, {staff_id})
            """
            self.cursor.execute(query_for_insertion)
            self.db_connection.commit()

        # Return the list of names of staff added
        return list_of_staff_ids

    
    def calculate_ticket_income(self, flight_trip_id):
        ticket_sum = self.cursor.execute(f"SELECT SUM(PricePaid) FROM TicketDetails WHERE FlightTrip_id = {flight_trip_id}").fetchone()
        return f"The total income from ticket sales for flight {flight_trip_id} is: £{ticket_sum[0]}"
