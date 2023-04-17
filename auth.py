import datetime

from flask import Blueprint
from m import db
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from flask import flash
from m import User
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    name = request.form.get('login')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(name=name).first()
    if not user or not check_password_hash(user.password, password):
        flash('Something went wrong'
              'Please check your login or password')
        return redirect(url_for('login.html'))
    return render_template('site_back.html')


@auth.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('login')
    password = request.form.get('password')
    user = User.query.filter_by(
        email=name).first()
    if user:
        flash('Account does not exist!')
        return redirect('registration.html')
    new_user = User(name=name, pssw=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('login.html'))

