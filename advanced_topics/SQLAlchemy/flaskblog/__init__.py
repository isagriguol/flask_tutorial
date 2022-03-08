# no terminal fazer:
# pip install flask-sqlalchemy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chavesecretaaleatoria'
# é preciso especificar a localização da base de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) # instância que constrói a base de dados

from flaskblog import routes