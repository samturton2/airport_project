import pyodbc
from os import system, name
from time import sleep
from database_connector import DBConnector
from passenger_ui import Passenger # import passengers class
from staff_ui import StaffUI_1, StaffUI_2
import pandas
from tabulate import tabulate


def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system("clear")

class LogIn(DBConnector):
    def __init__(self):
        super().__init__()
        self.passenger = False
        self.staff = False
        while True:
            print("  ______________________________________________ ")
            print(" | Choose option:                               |")
            print(" |                1. Passenger                  |")
            print(" |                2. Staff                      |")
            print(" |                3. Exit                       |")
            print(" |                                              |")
            answer = input(" |       ==> ").strip().upper()
            print(" |______________________________________________|")

            if answer not in ["1", "P", "2", "S", "3", "E"]:
                clear()
                continue

            if answer in ["3", "E"]:
                clear()
                exit()

            if answer[0] in ["1", "P"]:
                self.passenger = True
                # CALL THE PASSENGER LOG IN
                self.log_in()
                
            elif answer[0] in ["2", "S"]:
                self.staff = True
                # CALL THE STAFF LOG IN
                self.log_in()
                


    def log_in(self):
        i = 0
        while True:
            i += 1


            print("  ______________________________________________ ")
            print(" |  Login Page                                  |")
            print(" |                                              |")
            username = input(" |        Username: ").strip()
            print(" |                                              |")
            password = input(" |        Password: ").strip()
            print(" |______________________________________________|")



            # LOAD IN THE RELEVANT PASSENGERS AND STAFF LOG IN DETAILS
            if self.staff:
                # IF STAFF ALSO LOAD IN THERE RANK
                login_details = self.cursor.execute(f"SELECT StaffUsername, StaffPassword, StaffLevel FROM StaffLogins WHERE StaffUsername = '{username}';").fetchone()
                if login_details == None:
                    print("\nUsername not recognised!\n")
                    continue
                login_details = list(login_details)

            elif self.passenger:
                login_details = self.cursor.execute(f"SELECT PassengerUsername, PassengerPassword FROM PassengerLogins WHERE PassengerUsername = '{username}';").fetchone()
                print(login_details)
                if login_details == None:
                    print("\nUsername not recognised!\n")
                    continue
                login_details = list(login_details)
                login_details.append(0)

            else:
                login_details = [0]



            if password != login_details[1]:
                print("\nPassword Incorrect\n")

            elif i > 5:
                # IF LOG IN FAILED 5 TIMES SHUT THEM OUT
                print(" You have been shut out of the system! ")
                exit()


            elif [username, password] == login_details[:2]:
                clear()
                print("  ______________________________________________ ")
                print(" |  Login Page                                  |")
                print(" |                                              |")
                print(" |           LOGIN SUCCESSFUL!                  |")
                print(" |               LOADING...                     |")
                print(" |                                              |")
                print(" |______________________________________________|")
                
                sleep(1.5)

                if self.staff:
                    if login_details[2] == 1:
                        # RUN STAFF 1 CAPABILITIES
                        retr = StaffUI_1()
                        if retr == "RETURNED LOGOUT":
                            return LogIn()
                        return login_details[0], login_details[1], login_details[2]

                    elif list(login_details)[2] == 2:
                        # RUN STAFF 2 CAPABILITIES
                        retr = StaffUI_2()
                        if retr == "RETURNED LOGOUT":
                            return LogIn()
                        return login_details[0], login_details[1], login_details[2]


                if self.passenger:
                    # RUN PASSENGER CAPABILITIES
                    Passenger()
                    return login_details[0], login_details[1], login_details[2]


if __name__ == '__main__':
    LogIn()