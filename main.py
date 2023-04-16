from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import datetime
from flask import render_template
from flask import request

db = SQLAlchemy()
app = Flask(__name__)
# app.config['SECRET_KEY'] = 'zyxw4342vut123srqpo89nmlkjihgf78213123edc1233ba'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///server.db'
db.init_app(app)


# class News(SqlAlchemyBase):
#     __tablename__ = 'news'
#
#     id = sqlalchemy.Column(sqlalchemy.Integer,
#                            primary_key=True, autoincrement=True)
#     title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
#     content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
#     created_date = sqlalchemy.Column(sqlalchemy.DateTime,
#                                      default=datetime.datetime.now)
#     is_private = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
#
#     user_id = sqlalchemy.Column(sqlalchemy.Integer,
#                                 sqlalchemy.ForeignKey("users.id"))
#     user = orm.relationship('User')
#
#     def __repr__(self):
#         return f'<users {self.id}>'


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    # about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = db.Column(db.String(50),
                      index=True, unique=True, nullable=True)
    hashed_password = db.Column(db.String(500), nullable=True)
    created_date = db.Column(db.DateTime,
                             default=datetime.datetime.now)

    def __repr__(self):
        return f'<users {self.id}>'


class Profiles(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True, )
    name = db.Column(db.String, nullable=True)
    old = db.Column(db.Integer)
    city = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<users {self.id}>'


user = {'name': 'your name'}


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
