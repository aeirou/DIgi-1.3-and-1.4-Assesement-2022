#main python file that runs everything

from flask import Flask
from flask_sqlalchemy import SQLAlchemy #database using SQLAlchemy

db = SQLAlchemy() 
DB_NAME = 'books.db' #the name of the database

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ThWmZq4t7w9z$C&F)J@NcRfUjXn2r5u8x/A%D*G-KaPdSgVkYp3s6v9y$B&E(H+M'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #f mak es anything in it string - this tells flask where the database is located
    db.init_app(app) #initialize the database by giving it flask apps????
    from .views import app #imports app from view.py file


    return app

