from app import db
from app import app
import datetime
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
import sys


# db.create_all()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    nickname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)