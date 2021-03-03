from flask import Flask
from app import *
from user.models import User


@app.route('/user/signup', METHODS=['GET'])
def signup():
    return User.signup()
