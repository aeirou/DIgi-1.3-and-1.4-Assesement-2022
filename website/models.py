#this is where the database is stored - tables, info   
from time import timezone
from . import db 
from datetime import datetime
from sqlalchemy.sql import func
#default=func.now() - func takes the current time and date and sets it as a default info so that the user doesn't need put it themselves.

class Book(db.Model): #the whole table

    __tablename__ = 'book' #names the table "book"

    id = db.Column( #the table columns #the primary key of the table
      db.Integer,
      primary_key=True
    )
    title = db.Column( #title of the books
      db.String(255),
      nullable=False,
      unique=False
    )
    author = db.Column( #the author of the book
      db.String(225),
      nullable=False,
      unique=False
    ) 
    # year_published = db.Column( #the year the books were published
    #   db.DateTime,
    #   nullable=True,
    #   unique=False,
    #   default= datetime.utcnow
    # )
    isbn = db.Column( #unqiue id at the back of the book
      db.Integer,
      nullable = False,
      unique=True
    )
    book_id = db.relationship(
      "Borrowed_Books",
      backref='borrowed_books', #connects to the table of the foreign key (borrowed_books)
      lazy=True
    )
class Borrower(db.Model): #for when borrowing the books

    __name__ = 'borrower'

    id = db.Column(
      db.Integer,
      primary_key=True
    )     
    fname = db.Column( #first name of the borrower 
      db.String(255),
      nullable=False,
      unique=False

    )
    lname = db.Column( #last name of the borrower
      db.String(225),
      nullable=False,
      unique=False

    )
    email = db.Column( #email of the borrower
      db.String(225),
      nullable=False
    )
    ph_number = db.Column( #phone number of the user
      db.Integer,
      nullable=False
    )
    borrower_id = db.relationship(
      "Borrowed_Books",
      backref='borrower', #connects to the table of the foreign key (borrowed_books)
      lazy=True
    )

class Borrowed_Books(db.Model):

    __name__ = 'borrowed_books'
    id = db.Column( #id of the borrowed book
      db.Integer,
      primary_key=True
    )
    loan_date = db.Column(
      db.DateTime(timezone=True),
      default=func.now(),
      nullable=False
    )
    due_date = db.Column(
      db.DateTime,
      nullable=False
    )
    returned_date = db.Column(
      db.DateTime,
      nullable=False
    ) 
    id_borrower = db.Column( #foreign key
      db.Integer,
      db.ForeignKey('borrower.id')
    )
    id_book = db.Column(
      db.Integer,
      db.ForeignKey('book.id')
    )

# class Lender(db.Model):
  
#     __name__ = 'lender'

#     id = db.Column( #the table columns #the primary key of the table
#         db.Integer,
#         primary_key=True
#       ) 
#     title = db.Column( #title of the books
#         db.String(255),
#         nullable=False,
#         unique=False
#       )
#     author = db.Column( #the author of the book
#         db.String(225),
#         nullable=False,
#         unique=False
#       ) 
#     year_published = db.Column( #the year the books were published
#         db.DateTime,
#         nullable=False,
#         unique=False
#       )
#     isbn = db.Column( #unqiue id at the back of the book
#         db.Integer,
#         nullable = False,
#         unique=True
#       )
#     book_id = db.relationship(
#         "Borrowed_Books",
#         backref='borrowed_books', #connects to the table of the foreign key (borrowed_books)
#         lazy=True
#       )