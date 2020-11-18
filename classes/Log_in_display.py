import pyodbc
from database_connector import DBConnector
from passenger_ui import Passenger # import passengers class
from staff_ui import StaffUI_1, StaffUI_2
import pandas
from tabulate import tabulate


class LogIn(DBConnector):
    def __init__(self):
        super().__init__()
        self.passenger = False
        self.staff = False
        while True:
            print("  ______________________________________________ ")
            print(" | Please enter:                                |")
            print(" |                1. Passenger                  |")
            print(" |                2. Staff                      |")
            print(" |                                              |")
            answer = input(" |       ==> ")
            print(" |______________________________________________|")

            if answer[0] in ["1", "p", "P"]:
                self.passenger = True
                # CALL THE PASSENGER LOG IN
                self.log_in()
                break
            elif answer[0] in ["2", "s", "S"]:
                self.staff = True
                self.log_in()
                # CALL THE STAFF LOG IN
                break
            else:
                print("not an option")


    def log_in(self):
        i = 0
        while True:
            i += 1
            print("  ______________________________________________ ")
            print(" |  Login Page                                  |")
            print(" |                                              |")
            username = input(" |        Username: ")
            print(" |                                              |")
            password = input(" |        Password: ")
            print(" |______________________________________________|")
            # LOAD IN THE RELAVENT PASSENGERS AND STAFF LOG IN DETAILS
            if self.staff:
                # IF STAFF ALSO LOAD IN THERE RANK
                login_details = self.cursor.execute(f"SELECT Username, UserPassword, Rank FROM Staff WHERE Username = '{username}';").fetchone()
            elif self.passenger:
                login_details = self.cursor.execute(f"SELECT Username, UserPassword FROM Passenger WHERE Username = '{username}';").fetchone()
            else:
                print("Need to select passenger or staff")

            if len(login_details) == 0:
                print("\nUsername not recognised!\n")
            elif password != list(login_details)[1]:
                print("\nPassword Incorrect\n")
            elif i > 5:
                # IF LOG IN FAILED 5 TIMES SHUT THEM OUT
                print(" You have been shut out of the system! ")
                break
            elif [username, password] == list(login_details):
                print("  ______________________________________________ ")
                print(" |  Login Page                                  |")
                print(" |                                              |")
                print(" |          LOGIN SUCCESSFUL!                   |")
                print(" |                                              |")
                print(" |______________________________________________|")
                if self.staff:
                    if list(login_details)[3] == 1:
                        # RUN STAFF 1 CAPABILITIES
                        StaffUI_1()
                    elif list(login_details)[3] == 2:
                        # RUN STAFF 2 CAPABILITIES
                        StaffUI_2()
                elif self.passenger:
                    # RUN PASSENGER CAPABILITES
                    Passenger()


if __name__ == '__main__':
    login = LogIn()