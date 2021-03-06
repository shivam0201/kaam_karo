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


@app.route('/login_developer')
def login_developer():
    return render_template('SIGNUP.html')


@app.route('/login_recruiter')
def login_recruiter():
    return render_template('RECRUITER_SIGNUP.html')


@app.route('/registration/<email_id>', methods=['GET', 'POST'])
def registration(email_id):
    return render_template('Registration.html', email=email_id)


@app.route('/user_profile/<emaill>', methods=['GET', 'POST'])
def user_profile(emaill):
    return render_template('profile_page.html', email=emaill)


@app.route('/test_page')
def test_page():
    return render_template('test_page.html')


@app.route('/questions')
def questions():
    return render_template('questions.html')


@app.route('/recruiter_home')
def recruiter_home():
    return render_template('recindex.html')

# <-------------------------------------------------section for the developer---------------------------------------------------------------->


@app.route('/login_validation_developer', methods=['POST'])
def login_validation_developer():
    users_developer = mongo.db.user
    l_email = request.form.get('l_email_d')
    l_passwd = request.form.get('l_password_d')
    login_user_developer = users_developer.find_one(
        {'email': l_email})
    for passwd in users_developer.find({'email': l_email}, {'password': 1, '_id': 0}):
        p_name = passwd['password']
    if login_user_developer:
        if p_name == l_passwd:
            return redirect(url_for('registration', email_id=l_email))
    return render_template('/SIGNUP.html', message1='Invalid username/password')


@app.route('/add_user_developer', methods=['POST', 'GET'])
def add_user_developer():
    if request.method == 'POST':
        users_d = mongo.db.user
        existing_user_developer = users_d.find_one(
            {'email': request.form.get('r_email_d')})
        if existing_user_developer is None:
            r_name = request.form.get('r_name_d')
            r_email = request.form.get('r_email_d')
            r_passwd = request.form.get('r_password_d')
            users_d.insert_one(
                {'name': r_name, 'email': r_email, 'password': r_passwd})
            return redirect('/login_developer')
        return render_template('/SIGNUP.html', message2='User already exists')


# <------------------------------------------------Section for the recruiter---------------------------------------------------------------->

@app.route('/login_validation_recruiter', methods=['POST', 'GET'])
def login_validation():
    users_r = mongo.db.employer
    l_email = request.form.get('l_email_r')
    l_passwd = request.form.get('l_password_r')
    login_user_r = users_r.find_one({'email': l_email})
    for passwd in users_r.find({'email': l_email}, {'password': 1, '_id': 0}):
        p_name = passwd['password']
    if login_user_r:
        if l_passwd == p_name:
            return redirect('recruiter_home')
    return render_template('/RECRUITER_SIGNUP.html', message3="Invalid username/password")


@app.route('/add_user_recruiter', methods=['POST'])
def add_user():
    if request.method == 'POST':
        users_r = mongo.db.employer
        existing_user_r = users_r.find_one(
            {'email': request.form.get('r_email_r')})
        if existing_user_r is None:
            r_name = request.form.get('r_name_r')
            r_email = request.form.get('r_email_r')
            r_passwd = request.form.get('r_password_r')
            users_r.insert_one(
                {'name': r_name, 'email': r_email, 'password': r_passwd})
            return redirect('/login_recruiter')
        return render_template('/RECRUITER_SIGNUP.html', message4="User already exists")


# trying if dynamic data could be fetched
@app.route('/user_info/<email_id>', methods=['POST', 'GET'])
def user_info(email_id):
    email = email_id
    info = mongo.db.user
    username = request.form.get('user_name')
    about = request.form.get('about')
    contact = request.form.get('phone_number')
    address = request.form.get('address')
    pin_code = request.form.get('postal_code')
    info.update_one({'email': email}, {'$set': {'username': username, 'about': about,
                                                'contact': contact, 'address': address, 'postal_code': pin_code}})
    return redirect(url_for('user_profile', emaill=email))


if __name__ == '__main__':
    app.run(debug=True)
