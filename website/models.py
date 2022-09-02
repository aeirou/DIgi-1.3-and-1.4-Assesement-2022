#this is where the database is stored - tables, info   

from enum import unique
from . import db 
from datetime import datetime
#from sqlalchemy.sql import func
#default=func.now() - func takes the current time and date and sets it as a default info so that the user doesn't need put it themselves.

class Book(db.Model): #the whole table

    __tablename__ = 'book' #names the table "book"

    id = db.Column( #the table columns #the primary key of the table
      db.integer,
      primary_key=True
    ) 

    title = db.Column( #title of the books
      db.string(255),
      nullable=False,
      unique=False
    )
    author = db.Column( #the author of the book
      db.string(225),
      nullable=False,
      unique=False
    ) 
    year_published = db.Column( #the year the books were published
      db.datetime,
      nullable=False,
      unique=False
    )
    isbn = db.Comlumn( #unqiue id at the back of the book
      db.integer,
      nullable = False,
      unique=True
    )
    id_borrower = db.Column( #foreign key
      db.Integer,
      db.ForeignKey('borrower.id')
    )

class Borrower(db.Model):

    __name__ = 'borrower'

    id = db.Column(
      db.integer,
      primary_key=True
    )     
    fname = db.Column( #first name of the borrower 
      db.string(255),
      nullable=False,
      unique=False

    )
    lname = db.Column( #last name of the borrower
      db.string(225),
      nullable=False,
      unique=False

    )
    email = db.Column( #email of the borrower
      db.string(225),
      nullable=False
    )
    ph_number = db.Column( #phone number of the user
      db.integer,
      nullable=False
    )
    borrower_id = db.Relationship(
      "Book",
      backref='borrower', #connects to the table
      lazy=True
    )

class Borrowed_Books(db.Model):

    __name__ = 'borrowed_books'
    id = db.Column( #id of the borrowed book
      db.Integer,
      primary_key=True
    )
    loan_date = db.Columm(
      db.datetime,
      nullable=False
    )
    return_date = db.Column(
      db.datetime,
      nullable=False
    ) 





