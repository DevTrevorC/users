from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route('/')
def showAllUsers():
    users = User.get_all()
    print(users)
    return render_template("display_all.html", all_users = users, session = session)

@app.route('/add')
def addUser():
    return render_template("add_user.html")

@app.route('/edit')
def editUser():
    user = User.get_user(session['id'])
    print(user)
    return render_template('edit_user.html', user = user, session = session)

@app.route('/show')
def showUser():
    user = User.get_user(session['id'])
    return render_template('display_user.html', user = user, session = session)

@app.route('/mode', methods=["POST", "GET"])
def chooseMode():
    session['id'] = request.args.get('id')
    if request.args.get('mode') == 'edit':
        return redirect('/edit')
    else:
        return redirect('/show')

@app.route('/save', methods=["POST"])
def saveUser():
    data = {
        "firstName": request.form["firstName"],
        "lastName" : request.form["lastName"],
        "email" : request.form["email"]
    }
    User.add_user(data)
    return redirect('/')

