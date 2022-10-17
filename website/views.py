#the routes - where the visitor can go into
from flask import Blueprint, render_template, redirect, request, url_for, flash
from .models import Book
from . import db

views = Blueprint('views', __name__) #Blueprint is not an actual application - needs to be registered

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
      term = request.form.get('search') #takes what the person is searching

      return redirect(url_for('views.search', searchterm=term)) #redirects them to the page to see what they searched for

    return render_template('home.html')

@views.route('/lend', methods=['GET', 'POST'])
def lend():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        isbn = request.form.get('isbn')

        book = Book(title=title, author=author, isbn=isbn)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('views.books')) #redirects to the book page

    return render_template('lend.html')

@views.route('/search/<path:searchterm>')
def search(searchterm):
  term = "%{}%".format(searchterm)

  search = Book.query.filter((Book.title.like(term)) | (Book.author.like(term)) | (Book.isbn.like(term))).all()
  
  
  return render_template('search.html', results=search, searchterm=searchterm)


@views.route('/books')
def books():
    books = Book.query.limit(4).all() #orders the books by its title (alphabetical)
    return render_template('books.html', books=books)
  
# @app.route('/home')
# def search():
#     return render_template('search.html')


# @app.route('/error')
# def error():
#     return render_template('error.html')
