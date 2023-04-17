from flask import Blueprint
from app import db
from flask import render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/signup')
def signup():
    return render_template('registration.html')


# @auth.route('/logout')
# def logout():
#     return 'Logout'
