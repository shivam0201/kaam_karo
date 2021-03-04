from flask import Flask, render_template, url_for, request, redirect, jsonify, session
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/Employee'

mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/user')
def signup():
    if 'login_username' in session:
        return render_template('user_profile.html')
    else:
        return render_template('SIGNUP.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'email-id': request.form['login_email']})
    if login_user:
        if bcrypt.hashpw(request.form['login_password']) == login_user['password']:
            session['username'] = request.form['login_email']
            return render_template('user_profile.html')

    return 'Invalid username/password'


@app.route('/register', methods=['POST', "GET"])
def register():
    if request.method == 'POST':
        users = mongo.db.user
        existing_user = users.find_one(
            {'email-id': request.form['register_email']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(
                request.form['register_password'], bcrypt.gensalt())
            users.insert(
                {'email-id': request.form['register_email'], 'password': hashpass})
            session['username'] = request.form['register_email']
            return render_template('SIGNUP.html')

        return 'The user already exists'

    return render_template("SIGNUP.html")


if __name__ == '__main__':
    app.run(debug=True)
