# from curses import flash
from sre_constants import SUCCESS
from tkinter import Image
from flask import Flask, render_template, request, redirect, g, session, url_for,flash
from pip import main
from sqlalchemy import true
from flask_mail import Mail, Message
from config import mail_username, mail_password
import io
import base64
from sqlalchemy import true
from datetime import timedelta
import os
from flask_sqlalchemy import SQLAlchemy
import pickle
import sqlite3

# currentlocation = os.path.dirname(os.pathe.abspath(__file__))

app = Flask(__name__)

app.config['MAIL_SERVER'] = "smtp-mail.outlook.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSl'] = False
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password

app.secret_key = "abz"
app.permanent_session_lifetime = timedelta(minutes = 1)


mail = Mail(app)

@app.route("/")
def HomePage():
    return render_template('home.html')   


@app.route("/contactForm", methods = ['GET' , 'POST'])
def contactForm():
    if request.method == "POST":
        name = request.form.get('Name')
        email = request.form.get('Email')
        phone = request.form.get('Phone')
        message = request.form.get('Message')

        msg = Message(subject=f"Mail from{name}", body=f"Name: {name}\nE-Mail: {email}\nPhone: {phone}\n\n\n{message}", sender="oppanchayat5@outlook.com", recipients=['oppanchayat5@gmail.com'])
        mail.send(msg)
        return render_template("contactForm.html", success=True)

    return render_template('contactForm.html')


@app.route("/map-duration")
def map():
    return render_template('map.html', USER = session['name'])    

  
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST" :
        name = request.form['username']
        password = request.form['password']
        session['name'] = name

        connection = sqlite3.connect('Login.db')

        cursor = connection.cursor()

        query1 = "SELECT name, password from Login WHERE name = '"+name+"' AND password = '"+password+"'"
        cursor.execute(query1)
        results = cursor.fetchall()
        
        if len(results) == 1:
            return redirect(url_for('map'))
            # flash("You Are Successfully","LOGGED IN")
        else:
                # error = "invalid password"  
            return redirect("/login")
    return render_template('Login.html')


# @app.route("/wandering-solo")
# def solo():
#     return render_template('solo.html') 

# @app.route("/travelling")
# def travelling():
#     return render_template('travelling.html') 

@app.route("/Shimla")
def Shimla():
    return render_template('shimla.html') 

@app.route("/Delhi")
def Delhi():
    return render_template('delhi.html')

@app.route("/Chandigarh")
def Chandigarh():
    return render_template('Chandigarh.html')

@app.route("/Jabalpur")
def Jabalpur():
    return render_template('index.html') 
 

# Function for Convert Binary Data
# to Human Readable Format
def convertToBinaryData(filename):
	
# 	# Convert binary format to images
	# or files data
	with open(filename, 'rb') as file:
		blobData = file.read()
	return blobData

    
if __name__ == '__main__':
    app.run(debug=true)