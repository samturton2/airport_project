import pyodbc

class Accounting():

    def __init__(self):
        # connect to  DB
        self.server = "ldaijiw-micro.cdix33vx1qyf.eu-west-2.rds.amazonaws.com"
        self.database = "test_database"
        self.username = "ldaijiw"
        self.password = "DreamJLMSU743"

        self.start_connection()

        # ticket_details = self.cursor.execute("SELECT * FROM TicketDetails").fetchall()
        # for row in ticket_details:
        #     print(row)

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


    def calculate_ticket_income(self, flight_trip_id):
        ticket_sum = self.cursor.execute(f"SELECT SUM(PricePaid) FROM TicketDetails WHERE FlightTrip_id = {flight_trip_id}").fetchone()
        return f"The total income from ticket sales for flight {flight_trip_id} is: £{ticket_sum[0]}"

# test_run = Accounting()
# print(test_run.calculate_ticket_income(2))
