from flask import Flask, render_template, url_for, request, redirect, jsonify, session
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/Employee'
app.config['SECRET_KEY'] = 'development'

mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/user_profile')
def user_profile():
    return render_template('profile_page.html')


@app.route('/login_developer')
def login_developer():
    return render_template('SIGNUP.html')


@app.route('/login_recruiter')
def login_recruiter():
    return render_template('RECRUITER_SIGNUP.html')

# <---------------------------------------section for the developer---------------------------------------------------------------------------->


@app.route('/login_validation_developer', methods=['POST', 'GET'])
def login_validation_developer():
    users_developer = mongo.db.user
    l_email = request.form.get('l_email_d')
    l_passwd = request.form.get('l_password_d')
    login_user_developer = users_developer.find_one({'username': l_email})
    if login_user_developer:
        if users_developer.find_one({'password': l_passwd}):
            return redirect('/user_profile')
        return "Invalid password"
    return "No user found"


@app.route('/add_user_developer', methods=['POST'])
def add_user_developer():
    if request.method == 'POST':
        users_developer = mongo.db.user
        existing_user_developer = users_developer.find_one(
            {'username': request.form.get('r_email_d')})
        if existing_user_developer is None:
            r_email = request.form.get('r_email_d')
            r_passwd = request.form.get('r_password_d')
            users_developer.insert_one(
                {'username': r_email, 'password': r_passwd})
            return redirect('/login_developer')
        return "The user already exists"


# <------------------------------------------------Section for the recruiter---------------------------------------------------------------->

@app.route('/login_validation_recruiter', methods=['POST', 'GET'])
def login_validation():
    users_r = mongo.db.employer
    l_email = request.form.get('l_email_r')
    l_passwd = request.form.get('l_password_r')
    login_user_r = users_r.find_one({'username': l_email})
    if login_user_r:
        if users_r.find_one({'password': l_passwd}):
            return "Recruiter successfully logged in"
        return "Invalid password"
    return "No user found"


@app.route('/add_user_recruiter', methods=['POST'])
def add_user():
    if request.method == 'POST':
        users_r = mongo.db.employer
        existing_user_r = users_r.find_one(
            {'username': request.form.get('r_email_r')})
        if existing_user_r is None:
            r_email = request.form.get('r_email_r')
            r_passwd = request.form.get('r_password_r')
            users_r.insert_one({'username': r_email, 'password': r_passwd})
            return redirect('/login_recruiter')
        return "The user already exists"


if __name__ == '__main__':
    app.run(debug=True)
