from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import datetime
from flask import render_template

from flask import request

# from sqlalchemy import create_engine
# import sqlalchemy
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import Column, Integer, String, ForeignKey

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'zyxw4342vut123srqpo89nmlkjihgf78213123edc1233ba'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///server.sqlite'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    # about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = db.Column(db.String(50),
                      index=True, unique=True, nullable=True)
    password = db.Column(db.String(500), nullable=True)
    created_date = db.Column(db.DateTime,
                             default=datetime.datetime.now)

    def __init__(self, email: str, pssw: str, date: int):
        self.email = email
        self.pssw = pssw
        self.date = date

    def __repr__(self):
        return f'Пользователь {self.email}.' \
               f'Пароль {self.pssw}' \
               f'Дата {self.date}'


class Profiles(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    age = db.Column(db.Integer)
    city = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name: str, age: int, city: str, user_id: int):
        self.name = name
        self.age = age
        self.city = city
        self.user_id = user_id

    def __repr__(self):
        return f'Пользователь {self.name}.' \
               f'Возраст {self.age}' \
               f'Город {self.city}' \
               f'ID группы {self.user}'


@app.route('/')
def about():
    return render_template('site_back.html')


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    # if request.method == 'POST':
    return 'index'
    # return render_template('login.html')

# @app.route('/registration', methods=['POST', 'GET'])
# def registration():
#     # if request.method == 'POST':
#     return render_template('login.html')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
