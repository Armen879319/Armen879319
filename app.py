from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "key"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:1111@localhost/mysite"

db = SQLAlchemy(app)