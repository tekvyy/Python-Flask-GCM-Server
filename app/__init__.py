__author__ = 'tekvy'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.debug = True
app.secret_key = "09"


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

# create sqlAlchemy object

db = SQLAlchemy(app)
db.create_all()


import controllers