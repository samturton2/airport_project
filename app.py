from flask import Flask, jsonify, redirect, url_for, render_template, request, session
from classes.Log_in_display import LogIn
from classes.flight_trip_manager import FlightTripManager
import datetime
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/staffhome/")
def staffhome():
    return render_template('staff_home.html')


@app.route("/aboutus/")
def about_us():
    return render_template('aboutus.html')

# if any error occurs then redirects to error message page
@app.errorhandler(Exception)
def error_occured(error):
    return render_template('error.html')




@app.route("/loginpage/", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        print("POST")
        #session.pop('user_id')
        r_username = request.form['username']
        r_password = request.form['password']

        
        test_login = LogIn()

        try:
            test_username, test_password = test_login.log_in(r_username, r_password)
        except:
            return redirect(url_for('login'))
        
        else:
            if r_username == test_username and r_password == test_password:
                return redirect('/staffhome/')
            return redirect(url_for('login'))

        return redirect(url_for('login'))

    return render_template("login.html")


'''
FLIGHT TRIP MANAGER
'''

@app.route("/ftm/")
def flighttripmanager():
    return render_template('ftm_home.html')

@app.route("/ftm/createflighttrip/", methods = ["GET", "POST"])
def createflighttrip():
    if request.method == "POST":

        departuretime_str = request.form['departuretime']
        departuretime_dt = datetime.datetime.strptime(departuretime_str, '%Y-%m-%dT%H:%M')
       
        arrivalairport = request.form['arrivalairport']
        ticketprice = request.form['ticketprice']
        ticketdiscount = request.form['ticketdiscount']

        ftm = FlightTripManager()
        return_value = ftm.create_flight_trip(departuretime_dt, arrivalairport, ticketprice, ticketdiscount)
        print(return_value)

        if type(return_value) == int:
            succes_msg_str = f"Your flight to airport {arrivalairport} has FlightTrip ID {return_value}brbrRemember to assign an aircraft"
            return redirect(f'/ftm/success/{succes_msg_str}')

    return render_template('ftm_createflighttrip.html')


@app.route("/ftm/assignaircraft/", methods = ["GET", "POST"])
def assignaircraft():
    if request.method == "POST":
        r_flight_trip_id = request.form['flight_trip_id']

        ftm = FlightTripManager()
        return_value = ftm.assign_aircraft(r_flight_trip_id)

        if type(return_value) == int:
            succes_msg_str = f"Aircraft {return_value} assigned to FlightTrip {r_flight_trip_id}"
            return redirect(f'/ftm/success/{succes_msg_str}')
   
    return render_template("ftm_assignaircraft.html")


@app.route("/ftm/changeaircraft/", methods = ["GET", "POST"])
def changeaircraft():
    if request.method == "POST":
        r_flight_trip_id = request.form['flight_trip_id']

        ftm = FlightTripManager()
        return_value = ftm.change_aircraft(r_flight_trip_id)
        print(return_value)
        if type(return_value) == int:
            succes_msg_str = f"Aircraft {return_value} assigned to FlightTrip {r_flight_trip_id}"
            return redirect(f'/ftm/success/{succes_msg_str}')

    return render_template("ftm_changeaircraft.html")


@app.route("/ftm/flighttripincome/", methods = ["GET", "POST"])
def flighttripincome():
    if request.method == "POST":
        r_flight_trip_id = request.form['flight_trip_id']

        ftm = FlightTripManager()
        return_string = ftm.calculate_ticket_income(r_flight_trip_id)
        return redirect(f'/ftm/success/{return_string}')

    return render_template('ftm_flighttripincome.html')


@app.route("/ftm/checkstaffavailability/")
def checkstaffavailability():
    ftm = FlightTripManager()
    staff_list = ftm.check_staff_availability()
    
    html_insert = '''
    <table style = "width:50%">
        <tr>
            <th>Staff ID</th>
            <th>First Name</th>
            <th>Age</th>
        </tr>
    '''

    for staff_member in staff_list:
        html_insert = html_insert + '<tr>'
        for attribute in staff_member:
            html_insert = html_insert + f"<td>{attribute}</td>"
        html_insert = html_insert + "</tr>"



    return render_template('ftm_checkstaffavailability.html', text = html_insert)


@app.route("/ftm/assignstaff/", methods = ["GET", "POST"])
def assignstaff():
    if request.method == "POST":

     
       
        flighttripid = request.form['flighttripid']
        staffidlist_str = request.form['staffidlist'].replace(' ', '')

        print(staffidlist_str)
        
        staffid_listed = [int(x) for x in staffidlist_str.split(',')]
        print(staffid_listed)

        ftm = FlightTripManager()
        return_value = ftm.assign_staff_to_flight(flighttripid, staffid_listed)
        print(return_value)

        if type(return_value) == list:
             succes_msg_str = f"Successfully added Staff IDs {return_value} brbrto FlightTrip ID {flighttripid}"
             return redirect(f'/ftm/success/{succes_msg_str}')

    return render_template('ftm_assignstaff.html')



@app.route("/ftm/success/<scsmsg>")
def ftm_success(scsmsg):
    success_msg = "<h3>"+scsmsg.replace('brbr', '<br>')+"</h3>"
    return render_template("ftm_success.html", text=success_msg)


'''
BOOKING MANAGER
'''
@app.route("/bm/")
def bookingmanager():
    return render_template('bm_home.html')




if __name__ == "__main__":
    app.run(debug=True)