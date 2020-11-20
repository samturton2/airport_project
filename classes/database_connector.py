import pyodbc
from datetime import date

class DBConnector:
    def __init__(self):

        # connect to  DB
        self.server = "JaredPC\\JS_1"
        self.database = "Airport2"
        self.username = "sa"
        self.password = "passw0rd"

        self.start_connection()


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
            return "Connection Successful"