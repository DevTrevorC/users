from flask_app import app
from flask import render_template, redirect, request, session, flash
# from user import user

@app.route('/')
def showAllUsers():
    return render_template("display_all.html")

@app.route('/add')
def addUser():
    return render_template("add_user.html")