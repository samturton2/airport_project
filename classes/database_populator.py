from database_connector import DBConnector

class DBPopulator(DBConnector):
    def __init__(self):
        super().__init__()
        database_name = input("\nInput an exisitng database name or create a new database: ")
        try:
            self.cursor.execute(f"CREATE DATABASE {database_name};")
        except:
            pass