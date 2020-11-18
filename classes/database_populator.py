from database_connector import DBConnector

class DBPopulator(DBConnector):
    def __init__(self):
        super().__init__()

        # SQL QUERIES TO CREATE TABLES HERE