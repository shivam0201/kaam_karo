from flask import Flask, render_template, url_for, request, redirect, jsonify, session
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/Employee'
app.config['SECRET_KEY'] = 'development'

mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/user_profile')
def user_profile():
    return render_template('profile_page.html')


@app.route('/login')
def employee():
    return render_template('SIGNUP.html')


@app.route('/login_validation', methods=['POST', 'GET'])
def login_validation():
    users = mongo.db.user
    l_email = request.form.get('l_email')
    l_passwd = request.form.get('l_password')
    login_user = users.find_one({'username': l_email})
    if login_user:
        if users.find_one({'password': l_passwd}):
            return redirect('/user_profile')
        return "Invalid password"
    return "No user found"


@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        users = mongo.db.user
        existing_user = users.find_one(
            {'username': request.form.get('r_email')})
        if existing_user is None:
            r_email = request.form.get('r_email')
            r_passwd = request.form.get('r_password')
            users.insert_one({'username': r_email, 'password': r_passwd})
            return redirect('/login')
        return "The user already exists"


if __name__ == '__main__':
    app.run(debug=True)
