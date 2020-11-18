# TABLES: FLIGHT STAFF, FLIGHT TRIP, STAFF
# def assign_staff_to_flight():
#     # INPUT: FLIGHT TRIP ID
# 
#     # FIND HOW MANY STAFF REQUIRED
#     # CHECK WHO IS AVAILABLE
# 
#     # ASSIGN STAFF
#     # UPDATE FLIGHT STAFF TABLE
# 
#     # RETURN: LIST OF STAFF ASSIGNED
# 
# 
# # TABLES: FLIGHT TRIP, BOOKING DETAILS, FLIGHT STAFF, PASSENGERS, STAFF
# def flight_attendees():
#     # INPUT: FLIGHT TRIP ID
# 
#     # FIND ALL PASSENGERS/STAFF ON FLIGHT
# 
#     # RETURN: FLIGHT ATTENDEES LIST
import pyodbc


class FlightAttendees:
    def __init__(self, server, database, username, password):
        # Connects to the server automatically
        self.connection = pyodbc.connect(f"""
                DRIVER=ODBC Driver 17 for SQL Server;
                SERVER={server};
                DATABASE={database};
                UID={username};
                PWD={password}""")
        self.cursor = self.connection.cursor()


    # CHECKED LOCALLY
    # The return object is a tuple consisting of Passenger Names and Staff Names in lists
    def flight_attendees_list(self, flight_trip_id):
        passenger_query = f"""
        SELECT Passengers.Passenger_id, Passengers.FirstName, Passengers.LastName
        FROM FlightTrip
        INNER JOIN TicketDetails ON TicketDetails.FlightTrip_id = FlightTrip.FlightTrip_id
        INNER JOIN Passengers ON Passengers.Passenger_id = TicketDetails.Passenger_id
        WHERE FlightTrip.FlightTrip_id = {flight_trip_id};"""
        list_of_passengers = self.cursor.execute(passenger_query)
        retr_passengers = []
        for row in list_of_passengers:
            retr_passengers.append(row)

        staff_query = f"""
        SELECT Staff.Staff_id, Staff.FirstName, Staff.LastName
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
            self.connection.commit()

        # Adds the flight staff with flight id to the FlightStaff table
        for staff_id in list_of_staff_ids:
            query_for_insertion = f"""
            INSERT INTO FlightStaff (FlightTrip_id, Staff_id)
            VALUES ({flight_trip_id}, {staff_id})
            """
            self.cursor.execute(query_for_insertion)
            self.connection.commit()

        # Return the list of names of staff added
        return list_of_staff_ids


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


if __name__ == "__main__":
    pass
