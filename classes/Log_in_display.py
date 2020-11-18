import pyodbc
from classes.database_connector import DBConnector
#from classes.passenger_ui import Passenger # import passengers class
# import pandas
# from tabulate import tabulate


class LogIn(DBConnector):
    # def __init__(self):
    #     super().__init__()
    #     while True:
    #         print("  ______________________________________________ ")
    #         print(" | Please enter:                                |")
    #         print(" |                1. Passenger                  |")
    #         print(" |                2. Staff                      |")
    #         print(" |                                              |")
    #         answer = input(" |       ==> ")
    #         print(" |______________________________________________|")

    #         if answer[0] in ["1", "p", "P"]:
    #             Passenger()
    #             break
    #         elif answer[0] in ["2", "s", "S"]:
    #             self.log_in()
    #             break
    #         else:
    #             print("not an option")


    def log_in(self, username, password):
        i = 0
        while True:
            i += 1
            # print("  ______________________________________________ ")
            # print(" | Staff Login Page                             |")
            # print(" |                                              |")
            # username = input(" |        Username: ")
            # print(" |                                              |")
            # password = input(" |        Password: ")
            # print(" |______________________________________________|")
            
            login_details = self.cursor.execute(f"SELECT Username, UserPassword FROM Staff WHERE Username = '{username}';").fetchone()
            if len(login_details) == 0:
                print("\nUsername not recognised!\n")
            elif password != list(login_details)[1]:
                print("\nPassword Incorrect\n")
            elif i > 5:
                print(" You have been shut out of the system! ")
                break
            elif [username, password] == list(login_details):
                # print("  ______________________________________________ ")
                # print(" | Staff Login Page                             |")
                # print(" |                                              |")
                # print(" |          LOGIN SUCCESSFUL!                   |")
                # print(" |                                              |")
                # print(" |______________________________________________|")
                return username, password


if __name__ == '__main__':
    login = LogIn()