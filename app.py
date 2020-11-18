from flask import Flask, jsonify, redirect, url_for, render_template, request, session
from classes.Log_in_display import LogIn
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


'''
BOOKING MANAGER
'''
@app.route("/bm/")
def bookingmanager():
    return render_template('bm_home.html')



if __name__ == "__main__":
    app.run(debug=True)