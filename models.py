from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()


class Student(db.Model):
    __tablename__='students'
    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(), nullable=False)
    last_name=db.Column(db.String(), nullable=False)
    email=db.Column(db.String(), nullable=False)
    password=db.Column(db.String(), nullable=False)
    gender=db.Column(db.String())
    hobbies=db.Column(db.String())
    country=db.Column(db.String(), nullable=False)

def __init__(self, first_name, last_name, hobbies, email, password, gender, country):
    self.first_name=first_name
    self.last_name=last_name
    self.email=email
    self.password=password
    self.country=country
    self.hobbies=hobbies
    self.gender=gender

def __repr__(self):
    return f"{self.first_name}:{self.last_name}"