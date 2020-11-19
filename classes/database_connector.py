import pyodbc
from datetime import date

class DBConnector:
    def __init__(self):

        # connect to  DB
        self.server = "ldaijiw-micro.cdix33vx1qyf.eu-west-2.rds.amazonaws.com"
        self.database = "db_with_logins"
        self.username = "ldaijiw"
        self.password = "DreamJLMSU743"

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