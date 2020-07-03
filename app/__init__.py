from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATEBASE_URI'] = 'sqlite:///food.db'
db = SQLAlchemy(app)


wsgi_app = app.wsgi_app
from app import routes