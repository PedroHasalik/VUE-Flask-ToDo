from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

dbUser = os.environ['DBUSER']
dbPassword = os.environ['DBPASSWORD']

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+ dbUser + ':' + dbPassword + '@localhost/todos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.create_all()
CORS(app)

from todoBackend import controllers

