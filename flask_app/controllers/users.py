import re
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route('/')
def showAllUsers():
    users = User.get_all()
    print(users)
    return render_template("display_all.html", all_users = users)

@app.route('/add')
def addUser():
    return render_template("add_user.html")

@app.route('/save', methods=["POST"])
def saveUser():
    data = {
        "firstName": request.form["firstName"],
        "lastName" : request.form["lastName"],
        "email" : request.form["email"]
    }
    User.add_user(data)
    return redirect('/')