from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/tic_tac_toe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tic_tac_toe.db'
db = SQLAlchemy(app)

from app import routes, models
