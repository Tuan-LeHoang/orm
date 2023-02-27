from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return str(self.id) + " " + self.username

with app.app_context():
    db.create_all()

    # db.session.add(User('admin01', 'a1dmin@example.com'))
    # db.session.add(User('gues3t', 'gues2t@example.com'))
    db.session.commit()

    users = User.query.all()
    for user in users:
        print(user)
    # print(users)