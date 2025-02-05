from .extensions import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
     __tablename__ = 'User'
     id = db.Column(db.Integer, primary_key = True)
     name = db.Column(db.String(255), nullable = False)
     password = db.Column(db.String(255), nullable = False)
     high_score = db.Column(db.Integer, default = 0)
     speed_score = db.Column(db.Double, default = 0)


