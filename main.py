from flask import Blueprint
from app import db
from flask import render_template
main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('site_back.html')


@main.route('/profile')
def profile():
    return 'profile'
