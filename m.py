from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

from main import main as main_blueprint

app = Flask(__name__)
from auth import auth as auth_blueprint

app.register_blueprint(auth_blueprint)
from main import main as main_blueprint

app.register_blueprint(main_blueprint)
# app.config['SECRET_KEY'] = 'zyxw4342vut123srqpo89nmlkjihgf78213123edc1233ba'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///server.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.init_app(app)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),
                     index=True, unique=True, nullable=True)
    password = db.Column(db.String(500), nullable=False)
    created_date = db.Column(db.DateTime,
                             default=datetime.datetime.now)

    def __init__(self, name: str, pssw: str, date: int):
        self.name = name
        self.pssw = pssw
        self.date = date

    def __repr__(self):
        return f'Пользователь {self.name}.' \
               f'Пароль {self.pssw}' \
               f'Дата {self.date}'


class Profile(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    city = db.Column(db.String(100))

    def __init__(self, age: int, city: str):
        self.age = age
        self.city = city

    def __repr__(self):
        return f'Возраст {self.age}' \
               f'Город {self.city}' \
               f'ID группы {self.user}'
