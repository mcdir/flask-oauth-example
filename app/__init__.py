from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel, lazy_gettext

from app.oauth import OAuthSignIn

app = Flask(__name__)

db = SQLAlchemy(app)
lm = LoginManager(app)
lm.login_view = 'index'


babel = Babel(app)

db.create_all()

from app import views, models