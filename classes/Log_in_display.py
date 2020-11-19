import pyodbc
from database_connector import DBConnector
from passenger_ui import Passenger # import passengers class
from staff_ui import StaffUI_1, StaffUI_2
import pandas
from tabulate import tabulate
from cryptic import Cryptic

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
        crypto = Cryptic() # Create object of class
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
                login_details = list(self.cursor.execute(f"SELECT StaffUsername, StaffPassword, StaffLevel FROM StaffLogins WHERE StaffUsername = '{username}';").fetchone())
            elif self.passenger:
                login_details = list(self.cursor.execute(f"SELECT PassengerUsername, PassengerPassword FROM PassengerLogins WHERE PassengerUsername = '{username}';").fetchone())
                login_details.append(0)

            # DECRYPT THE PASSWORD AND LOAD IT BACK INTO THE LIST
            try:
                    password = crypto.decrypt(str(login_details.pop(1)))
                    login_details.insert(1, password)
            except:
                login_details = [0,0,0]

            if len(login_details) == 0:
                print("\nUsername not recognised!\n")
            elif password != login_details[1]:
                print("\nPassword Incorrect\n")
            elif i > 5:
                # IF LOG IN FAILED 5 TIMES SHUT THEM OUT
                print(" You have been shut out of the system! ")
                break
            elif [username, password] == login_details[:2]:
                print("  ______________________________________________ ")
                print(" |  Login Page                                  |")
                print(" |                                              |")
                print(" |          LOGIN SUCCESSFUL!                   |")
                print(" |                                              |")
                print(" |______________________________________________|")
                if self.staff:
                    if login_details[2] == 1:
                        # RUN STAFF 1 CAPABILITIES
                        StaffUI_1()
                        return login_details[0], login_details[1], login_details[2]
                    elif list(login_details)[2] == 2:
                        # RUN STAFF 2 CAPABILITIES
                        StaffUI_2()
                        return login_details[0], login_details[1], login_details[2]
                elif self.passenger:
                    # RUN PASSENGER CAPABILITIES
                    Passenger()
                    return login_details[0], login_details[1], login_details[2]


if __name__ == '__main__':
    login = LogIn()