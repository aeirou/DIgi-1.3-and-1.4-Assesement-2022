#the routes - where the visitor can go into
from crypt import methods
from re import template
from flask import Blueprint, render_template, redirect, request, url_for, flash
from .models import Book
from . import db

views = Blueprint('views', __name__) #Blueprint is not an actual application - needs to be registered

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')

        if title != str or author != str:
            return redirect(url_for('error'))
        else:
            return redirect(url_for('search'))

    return render_template('home.html')

@views.route('/lend', methods=['GET', 'POST'])
def lend():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        isbn = request.form.get('isbn')

        # if len(isbn) < 17:
        #     flash('Please try again.', category='error') #flash is a message that pops up when an error occours
        # elif len(isbn) > 17:
        #     flash('Please try again', category='error')
        # elif isbn != int:
        #     flash('ISBN not valid, please try again.', category='error')
        
        book = Book(title=title, author=author, isbn=isbn)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('views.books')) #redirects to the book page

    return render_template('lend.html')

@views.route('/books')
def books():
    books = Book.query.all() #orders the books by its title (alphabetical)
    return render_template('books.html', books=books)
  
# @app.route('/home')
# def search():
#     return render_template('search.html')


# @app.route('/error')
# def error():
#     return render_template('error.html')
