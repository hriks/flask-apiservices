import os
from flask import Flask

FLASK_HOST = '0.0.0.0'
FLASK_PORT = '8000'

DB_NAME = os.environ.get('DB_NAME', 'logindb')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'hriks9232')
DB_USERNAME = os.environ.get('DB_USERNAME', 'hriks')
DB_HOST = os.environ.get('DB_HOST', 'localhost')

DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(
    user=DB_USERNAME, pw=DB_PASSWORD, url=DB_HOST, db=DB_NAME)

DEBUG = os.environ.get('DEBUG', True)
SECRET_KEY = 'kjhadiuhx283728937X(*&@(*&'


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.config['CSRF_ENABLED'] = True
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True
    return app
